# GEO Array Digest (GAD)

Author: Sean Maden

Repo for all things GEO Array Digest (GAD), including code for the GAD Bot Twitter account ([@gadbot1](https://twitter.com/gadbot1)).

This repo uses the [Entrez Programming Utilities](https://www.ncbi.nlm.nih.gov/books/NBK179288/) software to query the [GEO](https://www.ncbi.nlm.nih.gov/geo/) API.

# GAD Bot

The GAD Bot is an automated messaging service that posts text summaries of public array datasets 
made available in GEO. It is maintained by Sean Maden (GitHub: [metamaden](https://github.com/metamaden), Twitter: [@MadenSean](https://twitter.com/MadenSean)), a Ph.D. candidate in Computational Biology at Oregon Health & Science University. 

This service was constructed using job scheduling, the [twitteR](https://cran.r-project.org/web/packages/twitteR/index.html) package, and a 
[snakemake](https://snakemake.readthedocs.io/en/stable/) workflow. Stay tuned for an upcoming [blog](https://metamaden.github.io/blog/) about how these components work together to make the resource.

