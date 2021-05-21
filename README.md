---
title: "GAD ReadMe"
author: "Sean Maden"
date: "20 May 2021"
output: html_document
---

# GEO Array Digest (GAD)

Author: Sean Maden

This is a repo for all things GEO Array Digest (GAD), including code for the GAD Bot Twitter account ([@gadbot1](https://twitter.com/gadbot1)). 

The GAD Bot is an automated messaging service that posts text summaries of public array datasets made available in GEO. It is maintained by Sean Maden (GitHub: [metamaden](https://github.com/metamaden), Twitter: [@MadenSean](https://twitter.com/MadenSean)), a Ph.D. candidate in Computational Biology at Oregon Health & Science University ([OHSU](https://www.ohsu.edu/people/sean-maden)).

The GAD service was constructed by scheduling queries to the [GEO](https://www.ncbi.nlm.nih.gov/geo/) API using the [Entrez Programming Utilities](https://www.ncbi.nlm.nih.gov/books/NBK179288/) software.
Automated status updates to the GAD Bot Twitter account are made using the [twitteR](https://cran.r-project.org/web/packages/twitteR/index.html) R package in a [snakemake](https://snakemake.readthedocs.io/en/stable/) workflow. 

Stay tuned for an upcoming [blog](https://metamaden.github.io/blog/) about how these components work together to make the GAD and GAD Bot resources.

```{r, echo = TRUE, message = TRUE}
knitr::kable(read.csv("inst/data/arraymetadf.csv"), align = "c")
```

# Array platforms

Details about the array platforms included in digests are provided in the manifest table at `inst/data/arraymetadf.csv`. 
The current version of the array platforms manifest looks like this:

---
accession,alias,type,description,release_date,spp
GPL13534,Illumina Infinium HM450 BeadChip,DNAm,Major array platform probing DNA methylation at roughly 480k CpG loci.,13-May-11,human
GPL21145,Illumina Infinium EPIC/HM850 BeadChip,DNAm,Major array platform probing DNA methylation at roughly 850k CpG loci.,16-Nov-15,human
GPL570,Affymetrix Human Genome U133 Plus 2.0 Array,expression,Major human gene expression/transcript profiling array using oligonucleotide assays.,3-Nov-03,human
GPL10558,Illumina HumanHT-12 V4.0 expression beadchip,expression,Major human gene expression/transcript profiling array using oligonucleotide beads.,17-Jan-10,human
GPL96,Affymetrix Human Genome U133A Array,expression,Major human gene expression/transcript profiling array using oligonucleotide assays.,3/11/02,human
---
