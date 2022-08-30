#!/usr/bin/env python3
# Author: Francois Aguet
import numpy as np
from collections import defaultdict
import argparse
import os
import gzip

class Exon:
    def __init__(self, exon_id, number, transcript, start_pos, end_pos):
        self.id = exon_id
        self.number = int(number)
        self.transcript = transcript
        self.start_pos = start_pos
        self.end_pos = end_pos

class Transcript:
    def __init__(self, transcript_id, transcript_name, transcript_type, gene, start_pos, end_pos):
        self.id = transcript_id
        self.name = transcript_name
        self.type = transcript_type
        self.gene = gene
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.exons = []

class Gene:
    def __init__(self, gene_id, gene_name, gene_type, chrom, strand, start_pos, end_pos):
        self.id = gene_id
        self.name = gene_name
        self.biotype = gene_type
        self.chr = chrom
        self.strand = strand
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.transcripts = []

class Annotation:
    def __init__(self, gtfpath):
        """Parse GTF and construct gene/transcript/exon hierarchy"""

        if gtfpath.endswith('.gtf.gz'):
            opener = gzip.open(gtfpath, 'rt')
        else:
            opener = open(gtfpath, 'r')

        self.genes = []
        with opener as gtf:
            for row in gtf:
                row = row.strip().split('\t')

                if row[0][0] == '#': continue # skip header

                # GTF
                # 0. seqname - name of the chromosome or scaffold;
                # 1. source - name of the program that generated this feature, or the data source (database or project name)
                # 2. feature - feature type name, e.g. Gene, Variation, Similarity
                # 3. start - Start position* of the feature, with sequence numbering starting at 1.
                # 4. end - End position* of the feature, with sequence numbering starting at 1.
                # 5. score - A floating point value.
                # 6. strand - defined as + (forward) or - (reverse).
                # 7. frame - One of '0', '1' or '2'.
                # 8. attribute - A semicolon-separated list of tag-value pairs

                chrom = row[0]
                annot_type = row[2]
                start_pos = int(row[3])
                end_pos  = int(row[4])
                strand = row[6]

                # https://note.nkmk.me/en/python-slice-usage/
                # x = [x for x in range(1, 11)]
                # print(x[:-1])
                # print(row[8])
                # print(row[8].replace('"', '').replace('_biotype', '_type').split(';'))
                # print(row[8].replace('"', '').replace('_biotype', '_type').split(';')[:-1])
                # quit()

                attributes = defaultdict(list)
                # remove double quotes, replace biotype with type, split on semicolons, and remove last entry
                for a in row[8].replace('"', '').replace('_biotype', '_type').split(';')[:-1]:
                    # print(a)
                    # strip removes all leading and trailing whitespaces when there are no args
                    kv = a.strip().split(' ')
                    # print(kv)
                    # quit()
                    # if a tag is named "tag", create list
                    if kv[0]!='tag':
                        attributes[kv[0]] = kv[1]
                    else:
                        attributes['tags'].append(kv[1])

                # print(attributes)
                # quit()

                if annot_type == 'gene':
                    # gene_id must be present
                    assert 'gene_id' in attributes
                    # if gene_name is missing assign, create it and assign it the gene_id
                    if 'gene_name' not in attributes:
                        attributes['gene_name'] = attributes['gene_id']
                    gene_id = attributes['gene_id']

                    # create gene instance
                    g = Gene(gene_id, attributes['gene_name'], attributes['gene_type'],
                             chrom, strand, start_pos, end_pos)
                    # add additional attributes to gene
                    g.source = row[1]
                    g.phase = row[7]
                    g.attributes_string = row[8].replace('_biotype', '_type')
                    # assign g to genes attributes for Annotation instance
                    self.genes.append(g)
                    # print(g.id)

                # same approach as gene
                elif annot_type == 'transcript':
                    assert 'transcript_id' in attributes
                    if 'transcript_name' not in attributes:
                        attributes['transcript_name'] = attributes['transcript_id']
                    transcript_id = attributes['transcript_id']
                    t = Transcript(attributes.pop('transcript_id'), attributes.pop('transcript_name'),
                                   attributes.pop('transcript_type'), g, start_pos, end_pos)
                    # include all attributes
                    t.attributes = attributes
                    # this relies on a sorted GTF file where there gene appears first
                    # followed by each transcript
                    g.transcripts.append(t)
                    # print(g.id)
                    # quit()

                elif annot_type == 'exon':
                    if 'exon_id' in attributes:
                        e = Exon(attributes['exon_id'], attributes['exon_number'], t, start_pos, end_pos)
                        # print(f"exon_id available as {attributes['exon_id']}")
                        # print("{} {}".format(str(len(t.exons)+1), len(t.exons)+1))
                    else:
                        e = Exon(str(len(t.exons)+1), len(t.exons)+1, t, start_pos, end_pos)
                        # print("exon_id not available")
                    # exons belong to transcript
                    t.exons.append(e)

                # print an update after 1000 genes
                if len(self.genes) % 1000 == 0:
                    # \r will work like your cursor has shifted to the beginning
                    print(f'\rParsing GTF: {len(self.genes)} genes processed', end='')
            print(f'\rParsing GTF: {len(self.genes)} genes processed')

        self.genes = np.array(self.genes)

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Parse GTF file')
    parser.add_argument('transcript_gtf', help='Transcript annotation in GTF format')
    args = parser.parse_args()

    annotation = Annotation(args.transcript_gtf)
    # numpy array of genes
    print(annotation.genes[0].id)
    print(annotation.genes[0].transcripts[0].id)
    print(annotation.genes[0].transcripts[0].exons[0].id)

