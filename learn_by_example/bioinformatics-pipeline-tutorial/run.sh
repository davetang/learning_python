#!/usr/bin/env bash

set -euo pipefail

prot=MYC

./01_digest_protein.py ${prot}.fasta ${prot}_pep.txt
./02_count_amino_acids.py ${prot}.fasta ${prot}_pep.txt ${prot}_count.tsv
./03a_plot_count.py ${prot}_count.tsv ${prot}_count.png
./03b_get_report.py ${prot}_count.tsv --output_file ${prot}_count_header.tsv

>&2 echo Done
exit 0

