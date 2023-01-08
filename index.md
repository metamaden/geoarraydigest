---
layout: default
---

<h1>GEO Array Digest</h1>

Welcome to the Geo Array Digest resource, or "GAD" for short!

<h1>About</h1>

Geo Array Digest (GAD) resource is an automated messaging service that monitors available of public array datasets made available in GEO database. The GAD service was constructed by scheduling queries to the [GEO](https://www.ncbi.nlm.nih.gov/geo/) API using the [Entrez Programming Utilities](https://www.ncbi.nlm.nih.gov/books/NBK179288/) software. Automated status updates to the GAD Bot Twitter account are made using the [twitteR](https://cran.r-project.org/web/packages/twitteR/index.html) R package in a [snakemake](https://snakemake.readthedocs.io/en/stable/) workflow. It is maintained by Sean Maden, PhD (GitHub: [metamaden](https://github.com/metamaden), Twitter: [@MadenSean](https://twitter.com/MadenSean)).

<h1>Array platforms</h1>

The digest targets a handful of the most numerous or active [platforms](https://www.ncbi.nlm.nih.gov/geo/browse/?view=platforms) on GEO. Details about the array platforms included in digests are provided in the manifest table at `~/data/arraymetadf.csv`. The current version of the array platforms manifest looks like this:

|accession|alias                                       |type      |description                                                                         |release_date|spp  |
|---------|--------------------------------------------|----------|------------------------------------------------------------------------------------|------------|-----|
|GPL13534 |Illumina Infinium HM450 BeadChip            |DNAm      |Major array platform probing DNA methylation at roughly 480k CpG loci.              |13-May-11   |human|
|GPL21145 |Illumina Infinium EPIC/HM850 BeadChip       |DNAm      |Major array platform probing DNA methylation at roughly 850k CpG loci.              |16-Nov-15   |human|
|GPL570   |Affymetrix Human Genome U133 Plus 2.0 Array |expression|Major human gene expression/transcript profiling array using oligonucleotide assays.|3-Nov-03    |human|
|GPL10558 |Illumina HumanHT-12 V4.0 expression beadchip|expression|Major human gene expression/transcript profiling array using oligonucleotide beads. |17-Jan-10   |human|
|GPL96    |Affymetrix Human Genome U133A Array         |expression|Major human gene expression/transcript profiling array using oligonucleotide assays.|3/11/02     |human|

<h1>Latest Digests:</h1>

<ul>
  {% for post in site.posts %}
    <li>
      <h2><a href="/geoarraydigest/{{ post.url }}">{{ post.title }}</a></h2>
      {{ post.excerpt }}
    </li>
  {% endfor %}
</ul>