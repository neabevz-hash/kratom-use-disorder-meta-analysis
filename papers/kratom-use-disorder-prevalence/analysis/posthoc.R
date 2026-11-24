# Post hoc analyses (deviations.md, D4), labelled as post hoc in the paper.
# 1. Within-study frequency gradient: kratom use disorder (DSM-5, >= 2 criteria) by daily dosing frequency in the
#    largest sample (Hill et al. 2024, S11): logistic regression on doses per day (1-6; the "other" group is left out).
#    A within-study comparison is not confounded by differences between studies in samples and instruments.
# 2. Sex: odds ratio (male vs female) for any use disorder in each sample that reports it (k < 3: not pooled).
# Run from the repository root: Rscript papers/kratom-use-disorder-prevalence/analysis/posthoc.R

suppressPackageStartupMessages({ library(dplyr); library(readr); library(ggplot2); library(metafor) })
paper <- "papers/kratom-use-disorder-prevalence"
res_dir <- file.path(paper, "analysis", "results"); fig_dir <- file.path(paper, "analysis", "figures")
est <- read_csv(file.path(paper, "forms", "estimates.csv"), show_col_types = FALSE)

doses <- c("once daily users" = 1, "twice daily users" = 2, "three times daily users" = 3,
           "four times daily users" = 4, "five times daily users" = 5, "six times daily users" = 6)
fr <- est %>% filter(sample_id == "S11", subgroup %in% names(doses)) %>%
  mutate(doses = doses[subgroup], pct = 100 * cases / n,
         lo = 100 * mapply(function(x, m) binom.test(x, m)$conf.int[1], cases, n),
         hi = 100 * mapply(function(x, m) binom.test(x, m)$conf.int[2], cases, n)) %>% arrange(doses)
g1 <- glm(cbind(cases, n - cases) ~ doses, data = fr, family = binomial)
ci <- suppressMessages(confint.default(g1))
trend <- tibble(analysis = "S11 (Hill 2024): any KUD by doses per day (1-6)", k_groups = nrow(fr), n = sum(fr$n),
                OR_per_dose = round(exp(coef(g1)[2]), 2), lo = round(exp(ci[2, 1]), 2), hi = round(exp(ci[2, 2]), 2),
                p = signif(summary(g1)$coefficients[2, 4], 3),
                pct_1_dose = round(fr$pct[1], 1), pct_5_6_doses = round(100 * sum(fr$cases[fr$doses >= 5]) / sum(fr$n[fr$doses >= 5]), 1))
write_csv(fr %>% select(doses, cases, n, pct, lo, hi), file.path(res_dir, "posthoc_frequency_groups.csv"))
write_csv(trend, file.path(res_dir, "posthoc_frequency_trend.csv"))

sx <- est %>% filter(subgroup %in% c("male", "female"), level == "L1") %>%
  select(sample_id, subgroup, cases, n) %>% tidyr::pivot_wider(names_from = subgroup, values_from = c(cases, n))
sex <- sx %>% rowwise() %>% mutate(
  OR = (cases_male / (n_male - cases_male)) / (cases_female / (n_female - cases_female)),
  se = sqrt(1 / cases_male + 1 / (n_male - cases_male) + 1 / cases_female + 1 / (n_female - cases_female)),
  lo = exp(log(OR) - 1.96 * se), hi = exp(log(OR) + 1.96 * se),
  pct_male = 100 * cases_male / n_male, pct_female = 100 * cases_female / n_female) %>% ungroup() %>%
  mutate(across(c(OR, lo, hi, pct_male, pct_female), ~ round(.x, 2)))
write_csv(sex %>% select(-se), file.path(res_dir, "posthoc_sex.csv"))

g <- ggplot(fr, aes(x = doses, y = pct)) + geom_point(aes(size = n)) +
  geom_errorbar(aes(ymin = lo, ymax = hi), width = 0.15) + geom_line(linetype = 2) +
  scale_x_continuous(breaks = 1:6) + scale_size_continuous(range = c(1.5, 4), guide = "none") +
  labs(x = "Kratom doses per day", y = "Kratom use disorder (DSM-5, ≥ 2 criteria), % (95% CI)") +
  theme_minimal(base_size = 10)
ggsave(file.path(fig_dir, "posthoc_frequency.pdf"), g, width = 5, height = 3.5)
ggsave(file.path(fig_dir, "posthoc_frequency.png"), g, width = 5, height = 3.5, dpi = 300)
print(trend); print(sex)
