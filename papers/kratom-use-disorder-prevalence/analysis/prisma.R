# PRISMA 2020 flow diagram (new studies via databases, search engines and citation searching).
# Reads fulltext/prisma_counts.json, forms/samples.csv and analysis/data/primary.csv; writes analysis/figures/prisma.{png,pdf}.
# Template: papers/sports-betting-prevalence/analysis/prisma.R.
# Run from the repository root: Rscript papers/kratom-use-disorder-prevalence/analysis/prisma.R

suppressPackageStartupMessages({ library(ggplot2); library(jsonlite) })
paper <- "papers/kratom-use-disorder-prevalence"
pc <- fromJSON(file.path(paper, "fulltext", "prisma_counts.json"))
fig_dir <- file.path(paper, "analysis", "figures")
fmt <- function(x) prettyNum(x, big.mark = ",")

src_names <- c(pubmed = "PubMed", europepmc = "Europe PMC", openalex = "OpenAlex",
               openalex_non_en = "OpenAlex, non-English queries", s2 = "Semantic Scholar", scopus = "Scopus (API)",
               crossref = "Crossref", citations = "Reference lists of 7 syntheses", datacite = "DataCite",
               openaire = "OpenAIRE", core = "CORE")
by_src <- unlist(pc$identification$records_per_source)
src_txt <- paste(sprintf("%s (n = %s)", src_names[names(by_src)], fmt(by_src)), collapse = "\n")
rb <- pc$identification$removed_before_screening
excl <- unlist(pc$screening$reports_excluded)
excl_names <- c("no use-disorder or dependence measure for kratom" = "No use-disorder or dependence measure",
                "design (review, qualitative without counts, case series, preclinical)" = "Design (review, qualitative,\ncase series, preclinical)",
                "no extractable counts" = "No extractable counts",
                "no estimate for people who use kratom" = "No estimate for people who use kratom",
                "duplicate or component of another report" = "Duplicate or component of another report",
                "sample recruited because of kratom problems" = "Recruited because of kratom problems")
excl <- excl[order(-excl)]
excl_txt <- paste(sprintf("%s (n = %s)", excl_names[names(excl)], fmt(excl)), collapse = "\n")
s <- read.csv(file.path(paper, "forms", "samples.csv"), colClasses = "character")
prim <- read.csv(file.path(paper, "analysis", "data", "primary.csv"), colClasses = "character")
studies_txt <- sprintf("Studies included in review (n = %d)\nReports of included studies (n = %d)\nIndependent samples (n = %d)\nSamples in the meta-analyses (n = %d)",
                       length(unique(s$study_id)), pc$screening$reports_included, nrow(s), length(unique(prim$sample_id)))
sc <- pc$screening
boxes <- data.frame(
  x = c(1, 3, 1, 3, 1, 3, 1, 3, 1), y = c(9, 9, 7, 7, 5, 5, 3, 3, 1), w = 1.9,
  h = c(2.1, 1.3, 0.7, 0.7, 0.7, 0.7, 0.7, 1.4, 1.0),
  label = c(
    paste0("Records identified (n = ", fmt(pc$identification$records_total), "):\n", src_txt),
    paste0("Records removed before screening:\nDuplicate records (n = ", fmt(pc$identification$duplicates_removed),
           ")\nRemoved by automation tools (n = ", fmt(rb$non_study_records + rb$vendor_advertising + rb$outside_concept_b),
           "):\nno people or dependence term (n = ", fmt(rb$outside_concept_b), ")\nnon-study records (n = ",
           fmt(rb$non_study_records), ")\nvendor advertising (n = ", fmt(rb$vendor_advertising), ")"),
    paste0("Records screened\n(n = ", fmt(sc$records_screened), ")"),
    paste0("Records excluded\n(n = ", fmt(sc$records_excluded), ")"),
    paste0("Reports sought for retrieval\n(n = ", fmt(sc$reports_sought), ")"),
    paste0("Reports not retrieved\n(no open-access full text; n = ", fmt(sc$reports_not_retrieved), ")"),
    paste0("Reports assessed for eligibility\n(n = ", fmt(sc$reports_assessed), ")"),
    paste0("Reports excluded (n = ", fmt(sum(excl)), "):\n", excl_txt),
    studies_txt), stringsAsFactors = FALSE)
arrows <- data.frame(
  x = c(1, 1.95, 1, 1.95, 1, 1.95, 1, 1.95), y = c(9 - 1.05, 9, 7 - 0.35, 7, 5 - 0.35, 5, 3 - 0.35, 3),
  xend = c(1, 2.05, 1, 2.05, 1, 2.05, 1, 2.05), yend = c(7 + 0.35, 9, 5 + 0.35, 7, 3 + 0.35, 5, 1 + 0.5, 3))
p <- ggplot() +
  geom_rect(data = boxes, aes(xmin = x - w / 2, xmax = x + w / 2, ymin = y - h / 2, ymax = y + h / 2),
            fill = "white", colour = "black", linewidth = 0.3) +
  geom_text(data = boxes, aes(x = x, y = y, label = label), size = 2.3, lineheight = 0.95) +
  geom_segment(data = arrows, aes(x = x, y = y, xend = xend, yend = yend),
               arrow = arrow(length = unit(0.12, "cm"), type = "closed"), linewidth = 0.3) +
  annotate("text", x = -0.25, y = c(9, 6, 1), label = c("Identification", "Screening", "Included"),
           angle = 90, size = 2.8, fontface = "bold") +
  annotate("text", x = 2, y = 10.4, label = "Databases, search engines and citation searching", size = 2.8, fontface = "bold") +
  coord_cartesian(xlim = c(-0.4, 4), ylim = c(0.3, 10.6)) + theme_void()
ggsave(file.path(fig_dir, "prisma.png"), p, width = 6.5, height = 7.5, dpi = 300, bg = "white")
ggsave(file.path(fig_dir, "prisma.pdf"), p, width = 6.5, height = 7.5)
cat("PRISMA diagram written to", fig_dir, "\n")
