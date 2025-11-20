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