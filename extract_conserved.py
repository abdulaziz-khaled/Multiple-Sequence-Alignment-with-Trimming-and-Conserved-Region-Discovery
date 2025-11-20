#!/usr/bin/env python3
import sys
from Bio import SeqIO
from collections import Counter

if len(sys.argv) < 3:
    print("Usage: python extract_conserved.py <alignment.fasta> <threshold>")
    sys.exit(1)

infile = sys.argv[1]
threshold = float(sys.argv[2])

records = list(SeqIO.parse(infile, "fasta"))
if not records:
    print("No sequences found in", infile)
    sys.exit(1)

L = len(records[0].seq)
for r in records:
    if len(r.seq) != L:
        print("Error: sequences have different lengths")
        sys.exit(1)

cols = []
for i in range(L):
    col = [str(r.seq[i]) for r in records]
    cols.append(col)

conserved = [False] * L
for i, col in enumerate(cols):
    cnt = Counter(col)
    gap_chars = {'-', '.'}
    total = len(col)
    non_gap_counts = {k: v for k, v in cnt.items() if k not in gap_chars}
    if non_gap_counts:
        top_freq = max(non_gap_counts.values()) / total
    else:
        top_freq = 0.0

    if top_freq >= threshold:
        conserved[i] = True

cons_cols = [i + 1 for i, v in enumerate(conserved) if v]

regions = []
start = None
for idx in range(1, L + 1):
    if idx in cons_cols:
        if start is None:
            start = idx
        end = idx
    else:
        if start is not None:
            regions.append((start, end))
            start = None
if start is not None:
    regions.append((start, end))

with open("conserved_regions.bed", "w") as out:
    for s, e in regions:
        out.write(f"{infile}\t{s}\t{e}\n")

with open("conserved_columns.txt", "w") as out:
    out.write(" ".join(map(str, cons_cols)) + "\n")

from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

out_records = []
for r in records:
    seq_pieces = []
    for s, e in regions:
        seq_pieces.append(str(r.seq[s - 1:e]))
    newseq = "".join(seq_pieces)
    out_records.append(SeqRecord(Seq(newseq), id=r.id, description="conserved_blocks"))

SeqIO.write(out_records, "conserved_regions.fasta", "fasta")

print("Done.")
print(f"Total columns: {L}")
print(f"Conserved columns: {len(cons_cols)}")
print(f"Regions found: {len(regions)}")
for r in regions:
    print(f" - {r[0]}-{r[1]}")
