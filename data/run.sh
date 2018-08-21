#!/usr/bin/env bash

# create example comma-delimited file
if [ ! -f iris.csv ]; then

   R --vanilla --quiet -e 'write.csv(iris, "iris.csv", quote = FALSE, row.names = FALSE)'

fi

# create example BAM file
if [ ! -f example.bam ]; then

   wget -c -N  http://s3-us-west-2.amazonaws.com/10x.files/samples/cell-exp/2.1.0/pbmc8k/pbmc8k_possorted_genome_bam.bam
   samtools view -b -s 0.00001 -o example.bam pbmc8k_possorted_genome_bam.bam
   samtools index example.bam

fi

