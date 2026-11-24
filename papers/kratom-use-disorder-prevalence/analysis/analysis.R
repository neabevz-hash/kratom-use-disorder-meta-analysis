# Prevalence of kratom use disorder and dependence among people who use kratom: meta-analysis (protocol v1.0, §13, §15-17).
#
# Reads analysis/data/primary.csv (one estimate per sample and level, chosen by the rules of §13 in build_levels.py)
# and analysis/data/level_estimates.csv (all cumulative estimates), and writes results to analysis/results/ and the
# forest plot to analysis/figures/. Template: papers/sports-betting-prevalence/analysis/analysis.R.
#
# Run from the repository root:  Rscript papers/kratom-use-disorder-prevalence/analysis/analysis.R

suppressPackageStartupMessages({
  library(metafor)
  library(lme4)
  library(dplyr)
  library(readr)
  library(ggplot2)
})

args <- commandArgs(trailingOnly = TRUE)
paper <- if (length(args) >= 1) args[1] else "papers/kratom-use-disorder-prevalence"
res_dir <- file.path(paper, "analysis", "results")
fig_dir <- file.path(paper, "analysis", "figures")
dir.create(res_dir, showWarnings = FALSE, recursive = TRUE)
dir.create(fig_dir, showWarnings = FALSE, recursive = TRUE)
MIN_K <- 3   # §15b: a pooled estimate needs at least three independent samples

prim <- read_csv(file.path(paper, "analysis", "data", "primary.csv"), show_col_types = FALSE) %>%
  mutate(regular = ifelse(tolower(regular_use_required) %in% c("no", "nr", "na", ""), "no", "yes"),
         grey = ifelse(pub_status == "journal", "journal", "grey"))
allest <- read_csv(file.path(paper, "analysis", "data", "level_estimates.csv"), show_col_types = FALSE)

pct <- function(x) round(100 * x, 1)

pool <- function(d, label) {
  if (nrow(d) < MIN_K) {
    return(tibble(analysis = label, k = nrow(d), n = sum(d$n), cases = sum(d$cases), prev = NA, lo = NA, hi = NA,
                  pi_lo = NA, pi_hi = NA, tau2 = NA, I2 = NA, note = "k < 3: not pooled"))
  }
  conv <- TRUE
  m <- withCallingHandlers(tryCatch(rma.glmm(xi = cases, ni = n, data = d, measure = "PLO", method = "ML"),
                                    error = function(e) NULL),
                           warning = function(w) { if (grepl("converge", conditionMessage(w))) conv <<- FALSE
                                                   invokeRestart("muffleWarning") })
  if (!is.null(m) && conv) {
    p <- predict(m, transf = transf.ilogit)
    return(tibble(analysis = label, k = m$k, n = sum(d$n), cases = sum(d$cases), prev = pct(p$pred), lo = pct(p$ci.lb),
                  hi = pct(p$ci.ub), pi_lo = pct(p$pi.lb), pi_hi = pct(p$pi.ub), tau2 = round(m$tau2, 3),
                  I2 = round(m$I2, 1), note = ""))
  }
  # rma.glmm did not converge: the same binomial-normal model fitted with lme4 (bobyqa); Wald CI, PI from tau
  f <- glmer(cbind(cases, n - cases) ~ 1 + (1 | sample_id), data = d, family = binomial,
             control = glmerControl(optimizer = "bobyqa"))
  b0 <- fixef(f)[1]; se <- sqrt(vcov(f)[1, 1]); tau <- as.data.frame(VarCorr(f))$sdcor[1]
  tq <- qt(0.975, nrow(d) - 2)
  tibble(analysis = label, k = nrow(d), n = sum(d$n), cases = sum(d$cases), prev = pct(plogis(b0)),
         lo = pct(plogis(b0 - 1.96 * se)), hi = pct(plogis(b0 + 1.96 * se)),
         pi_lo = pct(plogis(b0 - tq * sqrt(tau^2 + se^2))), pi_hi = pct(plogis(b0 + tq * sqrt(tau^2 + se^2))),
         tau2 = round(tau^2, 3), I2 = NA, note = "rma.glmm did not converge; lme4 glmer (bobyqa)")
}

pool_iv <- function(d, label) {   # sensitivity 9: inverse-variance REML on logits with Hartung-Knapp
  es <- escalc(measure = "PLO", xi = cases, ni = n, data = d)
  m <- rma(yi, vi, data = es, method = "REML", test = "knha")
  p <- predict(m, transf = transf.ilogit)
  tibble(analysis = label, k = m$k, n = sum(d$n), cases = sum(d$cases), prev = pct(p$pred), lo = pct(p$ci.lb),
         hi = pct(p$ci.ub), pi_lo = pct(p$pi.lb), pi_hi = pct(p$pi.ub), tau2 = round(m$tau2, 3), I2 = round(m$I2, 1),
         note = "IV REML-HK")
}

L1 <- filter(prim, level == "L1"); L2 <- filter(prim, level == "L2"); L3 <- filter(prim, level == "L3")

# ---------------------------------------------------------------- pooled estimates by level and subgroup (§15b)
pooled <- bind_rows(
  pool(L2, "L2 moderate-to-severe or dependence (primary)"),
  pool(L1, "L1 any use disorder"),
  pool(L3, "L3 severe use disorder"),
  pool(filter(L2, region == "Southeast Asia"), "L2, Southeast Asia"),
  pool(filter(L2, region == "North America"), "L2, North America"),
  pool(filter(L2, region == "Europe"), "L2, Europe"),
  pool(filter(L1, region == "North America"), "L1, North America"),
  pool(filter(L3, region == "North America"), "L3, North America"),
  pool(filter(L2, sample_type == "online_consumers"), "L2, online consumers"),
  pool(filter(L2, sample_type == "community_users"), "L2, community users")
)
write_csv(pooled, file.path(res_dir, "pooled.csv"))

# Region contrast (Southeast Asia vs North America; Europe k = 2 kept in the model as its own category)
mreg <- suppressWarnings(rma.glmm(xi = cases, ni = n, mods = ~ factor(region, levels = c("North America", "Southeast Asia", "Europe")),
                 data = L2, measure = "PLO", method = "ML"))
reg_test <- tibble(test = "L2 by region (GLMM)", QM = round(mreg$QM, 2), df = mreg$m, p = signif(mreg$QMp, 3),
                   OR_SEA_vs_NA = round(exp(coef(mreg)[2]), 2),
                   OR_SEA_lo = round(exp(mreg$ci.lb[2]), 2), OR_SEA_hi = round(exp(mreg$ci.ub[2]), 2),
                   OR_EUR_vs_NA = round(exp(coef(mreg)[3]), 2),
                   OR_EUR_lo = round(exp(mreg$ci.lb[3]), 2), OR_EUR_hi = round(exp(mreg$ci.ub[3]), 2))
write_csv(reg_test, file.path(res_dir, "subgroup_tests.csv"))

# ---------------------------------------------------------------- pre-specified multivariable model, all estimates (§15b)
# One sample per study here, so the multilevel model has random intercepts for samples (estimates in samples).
mm <- prim %>% mutate(level3 = factor(level, levels = c("L1", "L2", "L3")),
                      region3 = factor(region, levels = c("North America", "Southeast Asia", "Europe")),
                      regular = factor(regular, levels = c("no", "yes")))
fit <- glmer(cbind(cases, n - cases) ~ level3 + region3 + regular + (1 | sample_id), data = mm, family = binomial,
             control = glmerControl(optimizer = "bobyqa"))
cf <- summary(fit)$coefficients
ci <- suppressMessages(confint(fit, method = "Wald"))[rownames(cf), ]
multi <- tibble(term = rownames(cf), OR = round(exp(cf[, 1]), 2), lo = round(exp(ci[, 1]), 2), hi = round(exp(ci[, 2]), 2),
                p = signif(cf[, 4], 3))
write_csv(multi, file.path(res_dir, "multilevel_prespecified.csv"))
writeLines(capture.output(print(VarCorr(fit))), file.path(res_dir, "multilevel_varcorr.txt"))

# ---------------------------------------------------------------- sensitivity analyses on the primary outcome (§15c)
# D3: reports downloaded by hand by R1 (retrieval_log source = manual_pdf) -> samples whose main report is one of them
manual_reports <- read_csv(file.path(paper, "fulltext", "retrieval_log.csv"), show_col_types = FALSE) %>%
  filter(source == "manual_pdf") %>% pull(rec_id)
manual_samples <- read_csv(file.path(paper, "forms", "samples.csv"), show_col_types = FALSE) %>%
  mutate(main_report = sub(";.*", "", report_ids)) %>% filter(main_report %in% manual_reports) %>% pull(sample_id)
sens <- bind_rows(
  pool(filter(L2, code == "L2"), "1 DSM-5, SUDST or interview only (no scales, no ASSIST)"),
  pool(filter(L2, jbi_2 == "yes"), "2 probability, census or consecutive samples"),
  pool(filter(L2, jbi_6 == "yes"), "3 valid identification (JBI 6 = yes)"),
  pool(filter(L2, jbi_9 == "yes"), "4 response >= 60% or handled (JBI 9 = yes)"),
  pool(filter(L2, !sample_type %in% c("treatment_other_sud", "psychiatric_patients")), "5 excluding patients"),
  pool(filter(L2, recruitment_channel != "advocacy or vendor channels"), "6 excluding advocacy or vendor recruitment"),
  pool(filter(L2, grey == "journal"), "7 journal articles only"),
  pool(filter(L2, n >= 100), "8 excluding n < 100"),
  pool_iv(L2, "9 inverse-variance REML-HK"),
  pool(filter(L2, !sample_id %in% manual_samples), "11 excluding samples whose main report R1 downloaded by hand (D3)")
)
loo <- bind_rows(lapply(seq_len(nrow(L2)), function(i) pool(L2[-i, ], paste("10 leave out", L2$sample_id[i], L2$first_author[i]))))
sens <- bind_rows(sens, loo)
write_csv(sens, file.path(res_dir, "sensitivity.csv"))

# ---------------------------------------------------------------- meta-biases (§16)
es2 <- escalc(measure = "PLO", xi = cases, ni = n, data = L2)
mb <- rma(yi, vi, mods = ~ I(1 / sqrt(n)), data = es2, method = "REML", test = "knha")
mg <- rma.glmm(xi = cases, ni = n, mods = ~ grey, data = L2, measure = "PLO", method = "ML")
write_csv(tibble(test = c("logit prevalence ~ 1/sqrt(n) (REML-HK)", "journal vs grey literature (GLMM)"),
                 estimate = round(c(coef(mb)[2], coef(mg)[2]), 3), p = signif(c(mb$pval[2], mg$QMp), 3)),
          file.path(res_dir, "meta_bias.csv"))

# ---------------------------------------------------------------- descriptives and the estimates table
write_csv(prim %>% select(sample_id, first_author, year, country, region, sample_type, level, code, instrument,
                          time_frame, cases, n, pct, how), file.path(res_dir, "estimates_used.csv"))
write_csv(allest %>% filter(!paste(sample_id, level, instrument, time_frame) %in%
                              paste(prim$sample_id, prim$level, prim$instrument, prim$time_frame)),
          file.path(res_dir, "estimates_not_used.csv"))

# ---------------------------------------------------------------- forest plot, L2 by case definition (Figure 2)
# Panels: DSM-5 criteria (checklist, SUDST) vs dependence scales and ASSIST; filled points: the sample was restricted to
# regular users; dashed line in the DSM-5 panel: pooled estimate of sensitivity analysis 1.
dsm_pool <- sens$prev[startsWith(sens$analysis, "1 ")]
fp <- L2 %>% mutate(p = cases / n, ci = lapply(seq_len(n()), function(i) binom.test(cases[i], n[i])$conf.int),
                    lo = sapply(ci, `[`, 1), hi = sapply(ci, `[`, 2),
                    panel = ifelse(code == "L2", "DSM-5 criteria (checklist or SUDST)", "Dependence scale or ASSIST"),
                    regular_lab = ifelse(regular == "yes", "Regular users only", "Any use"),
                    lab = sprintf("%s %s (%s, %s), n = %s", first_author, year, country, instrument, trimws(format(n, big.mark = ",")))) %>%
  mutate(panel = factor(panel, levels = c("DSM-5 criteria (checklist or SUDST)", "Dependence scale or ASSIST"))) %>%
  arrange(panel, p)
fp$lab <- factor(fp$lab, levels = rev(fp$lab))
vl <- tibble(panel = factor("DSM-5 criteria (checklist or SUDST)", levels = levels(fp$panel)), x = dsm_pool)
g <- ggplot(fp, aes(x = 100 * p, y = lab)) +
  geom_errorbarh(aes(xmin = 100 * lo, xmax = 100 * hi), height = 0.2) +
  geom_point(aes(shape = regular_lab), size = 2.4, fill = "black") +
  geom_vline(data = vl, aes(xintercept = x), linetype = 2) +
  facet_grid(panel ~ ., scales = "free_y", space = "free_y", labeller = label_wrap_gen(18)) +
  scale_shape_manual(values = c("Any use" = 1, "Regular users only" = 15), name = NULL) +
  scale_x_continuous(limits = c(0, 100), breaks = seq(0, 100, 25)) +
  labs(x = "Moderate-to-severe kratom use disorder or dependence, % (95% CI)", y = NULL) +
  theme_minimal(base_size = 10) + theme(strip.text.y = element_text(angle = 0), legend.position = "bottom")
ggsave(file.path(fig_dir, "forest_L2.pdf"), g, width = 7.5, height = 4.8)
ggsave(file.path(fig_dir, "forest_L2.png"), g, width = 7.5, height = 4.8, dpi = 300)

writeLines(capture.output(sessionInfo()), file.path(paper, "analysis", "sessionInfo.txt"))
print(pooled, width = 200)
print(reg_test, width = 200)
print(multi)
print(sens %>% select(analysis, k, prev, lo, hi, note), n = 40, width = 200)
