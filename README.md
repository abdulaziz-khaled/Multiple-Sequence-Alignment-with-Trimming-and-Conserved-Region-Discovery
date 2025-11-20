# Introduction
Thyroperoxidase (TPO) is a key enzyme involved in thyroid hormone biosynthesis, making its gene sequence an important target for molecular and bioinformatics studies. Due to natural sequence variations across species and isoforms, identifying reliable conserved regions within the TPO gene is essential for downstream applications such as primer design, comparative genomics, and functional analysis.

In this study, a complete workflow was established to process and refine TPO gene sequence data through multiple sequence alignment (MSA), sequence trimming, and conserved region discovery. Collected TPO sequences from various organisms were aligned using widely adopted alignment algorithms to reveal evolutionary conserved motifs. Subsequent trimming steps were applied to remove low-quality or misaligned regions, ensuring high-confidence alignment blocks suitable for further analysis.

The resulting conserved regions provide a robust foundation for future experimental and computational applications, including primer development, structural prediction, gene-based diagnostic assays, and reconstruction of phylogenetic trees to infer evolutionary relationships. This workflow demonstrates the effectiveness of integrating MSA, trimming, and conservation analysis to extract meaningful biological insights from sequence datasets.

## Materials and Methods
# Instruments and Materials
Instruments used in this study included a collection of `bioinformatics tools` applied for sequence retrieval, alignment, trimming, and conserved region identification. 
Sequence mining was performed using `NCBI BLAST`, while multiple sequence alignment (MSA) was conducted in `MEGA` using the `MUSCLE` algorithm. 
Sequence trimming and removal of low-quality alignment `blocks` were carried out using `Gblocks` under a `Linux` environment. 
Command-line processing and dataset manipulation were supported by `awk tool`, and conserved region extraction and parsing tasks were performed using a custom `Python script` built with the `Biopython` library. 
Data organization and text handling were completed using `Microsoft Excel`, `Notepad++`, and a `laptop computer`.
The material used in this study consisted of Thyroperoxidase (TPO) gene sequences obtained from the `NCBI database`. A total of 101 TPO gene sequences were retrieved through `BLAST` searches to capture sequence diversity across species. Additionally, datasets associated with `Gene ID: 7173` (human TPO) were downloaded in `FASTA format` for subsequent alignment, trimming, and conserved region analysis.

# DNA Sequence Data Mining
DNA sequence data collection in this study was conducted using two complementary approaches to ensure broad evolutionary coverage as well as high-quality reference alignment. 
The first dataset was obtained by mining TPO (Thyroperoxidase) gene sequences through `NCBI BLAST`, where the `Nucleotide` option was selected and keywords such as `“thyroperoxidase (TPO)”, "Human", “CDS”`, and related terms were used to retrieve sequences from multiple species. 
This search produced a diverse dataset of `101 TPO gene` sequences, which were downloaded in `FASTA format` and compiled into a single file for downstream processing. 
This dataset was subsequently analyzed through multiple sequence alignment (MSA), trimming, and conserved region detection.

In the second approach, a more focused dataset was collected by retrieving sequence entries associated with `Gene ID: 7173` (human TPO) directly from the `NCBI Gene` database. 
These sequences were also downloaded in `FASTA format` and treated as an independent dataset. A separate pipeline of MSA, trimming, and conserved region identification was performed on this dataset to provide high-resolution insights specific to the human TPO gene.
All downloaded FASTA sequences were organized using simple text editors such as `Notepad++`, with each sequence treated as an individual operational taxonomic unit (OTU) before being processed in the subsequent analytical steps.


