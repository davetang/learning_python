#!/usr/bin/env python3
import argparse
# https://docs.python.org/3/library/re.html
import re
import sys

def load_fasta(filename):
    """
    Load a protein with its metadata from a given .fasta file.
    """
    with open(filename, "r") as fasta_file:
        lines = fasta_file.read().splitlines()
    metadata = lines[0]
    sequence = "".join(lines[1:])
    print("Read {}".format(filename), file=sys.stderr)
    return metadata, sequence


def save_peptides(filename, peptides):
    """
    Write out the list of given peptides to a .txt file. Each line is a different peptide.
    """
    with open(filename, "w") as output_file:
        for peptide in peptides:
            output_file.write("{}\n".format(peptide))


# Trypsin cleaves the peptide bond between the carboxyl group of arginine (R)
# or the carboxyl group of lysine (K) and the amino group of the adjacent amino
# acid (https://pubmed.ncbi.nlm.nih.gov/22485945/).
#
# a missed cleavage is any uncut lysine/arginine peptide bond
# https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2664920/
def digest_protein(
    protein_sequence,
    enzyme_regex="[KR]",
    missed_cleavages=0,
    min_length=4,
    max_length=75
):
    """
    Digest a protein into peptides using a given enzyme. Defaults to trypsin.
    All the code is taken from https://github.com/wfondrie/mokapot/blob/master/mokapot/parsers/fasta.py.
    The only reason why I didn't use mokapot as a package is because I wanted to leave 
    any packaging out of this tutorial.
    """
    #
    # Find the cleavage sites
    #

    # https://docs.python.org/3/library/re.html#re.compile
    # compile a regex into a regular expression object, which can be used for
    # matching using its match(), search() and other methods
    enzyme_regex = re.compile(enzyme_regex)
    print("enzyme_regex is of type {}".format(type(enzyme_regex)))

    # https://docs.python.org/3/library/re.html#re.finditer
    # return an iterator yielding match objects over all non-overlapping
    # matches
    for m in enzyme_regex.finditer(protein_sequence):
        print(m.start(), m.end())

    sites = (
        [0]
        + [m.end() for m in enzyme_regex.finditer(protein_sequence)]
        + [len(protein_sequence)]
    )
    print("sites {}".format(sites), file=sys.stderr)

    # set items are unordered, immutable, and do not allow duplicate values.
    peptides = set()

    # Do the digest
    for start_idx, start_site in enumerate(sites):
        print(f'start_idx is {start_idx} and start_site is {start_site}')
        # if a cleavage is missed then a potentially longer cleavage may occur
        for diff_idx in range(1, missed_cleavages + 2):
            # jump to different sites
            end_idx = start_idx + diff_idx
            # skip if index is longer than list
            if end_idx >= len(sites):
                continue
            # end site is the next match
            end_site = sites[end_idx]
            # peptide sequence is the first match and the next match
            peptide = protein_sequence[start_site:end_site]
            # skip if peptide is not between wanted lengths
            if len(peptide) < min_length or len(peptide) > max_length:
                continue
            peptides.add(peptide)
            print(f"\t{peptide}")
    return peptides

# https://note.nkmk.me/en/python-args-kwargs-usage/
# use * or ** to accept variable-length arguments
# *args = arguments and **kwargs = keyword arguments (as dictionary)
def main(input_file, output_file, **kwargs):
    """
    Digest a protein and save the peptides.
    """
    _, protein_sequence = load_fasta(input_file)
    peptides = digest_protein(protein_sequence, **kwargs)
    save_peptides(output_file, peptides)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "input_file", 
        help="A .fasta file containing a protein."
    )
    parser.add_argument(
        "output_file", 
        help="A .txt output file to write the peptides to."
    )
    parser.add_argument(
        "--enzyme_regex", 
        help="A regex for the enzyme to use for the digest. E.g. [KR] for trypsin."
    )
    parser.add_argument(
        "--missed_cleavages", 
        type=int, 
        help="Number of missed cleavages for the digest."
    )
    parser.add_argument(
        "--min_length", 
        type=int, 
        help="Minimum length for a peptide to be considered valid."
    )
    parser.add_argument(
        "--max_length", 
        type=int, 
        help="Maximum length for a peptide to be considered valid."
    )
    kwargs = {k:v for k,v in vars(parser.parse_args()).items() if v}
    input_file = kwargs.pop("input_file")
    output_file = kwargs.pop("output_file")
    main(input_file, output_file, **kwargs)
