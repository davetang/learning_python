## README

The
[collapse_annotation.py](https://github.com/broadinstitute/gtex-pipeline/blob/master/gene_model/collapse_annotation.py)
script was written by Francois Aguet and as per the script's documentation:

>Collapse isoforms into single transcript per gene and remove overlapping
intervals between genes

A [virtual environment](https://docs.python.org/3/tutorial/venv.html) has been
  prepared for running this script. Run `create_venv.sh` to prepare the
  environment, `source` to activate it, and `deactivate` to deactivate.

```bash
./create_venv.sh
source my_venv/bin/activate
deactivate
```

Usage.

```
usage: collapse_annotation.py [-h]
                              [--transcript_blacklist TRANSCRIPT_BLACKLIST]
                              [--collapse_only] [--stranded]
                              transcript_gtf output_gtf

Collapse isoforms into single transcript per gene and remove overlapping
intervals between genes

positional arguments:
  transcript_gtf        Transcript annotation in GTF format
  output_gtf            Name of the output file

optional arguments:
  -h, --help            show this help message and exit
  --transcript_blacklist TRANSCRIPT_BLACKLIST
                        List of transcripts to exclude (e.g., unannotated
                        readthroughs)
  --collapse_only       Only collapse transcripts of each gene, do not remove
                        overlaps.
  --stranded            Only consider genes on the same strand when removing
                        overlaps.
```

Download GTF.

```bash
ver=41
wget -c https://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_human/release_${ver}/gencode.v${ver}.annotation.gtf.gz
```

Test.

```bash
./collapse_annotation.py gencode.v41.annotation.gtf.gz test.gtf
```

