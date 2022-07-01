#!/usr/bin/env bash

set -euo pipefail

check_depend (){
   tool=$1
   if [[ ! -x $(command -v ${tool}) ]]; then
     >&2 echo Could not find ${tool}
     exit 1
   fi
}

dependencies=(wget unzip R samtools)
for tool in ${dependencies[@]}; do
   check_depend ${tool}
done

# create example comma-delimited file
if [[ ! -f iris.csv ]]; then
   R --vanilla --quiet -e 'write.csv(iris, "iris.csv", quote = FALSE, row.names = FALSE)'
else
   >&2 echo iris.csv already exists
fi

# create example BAM file
if [[ ! -f example.bam ]]; then
   wget -c -N  http://s3-us-west-2.amazonaws.com/10x.files/samples/cell-exp/2.1.0/pbmc8k/pbmc8k_possorted_genome_bam.bam
   samtools view -b -s 0.00001 -o example.bam pbmc8k_possorted_genome_bam.bam
   samtools index example.bam
else
   >&2 echo example.bam already exists
fi

# Software carpentry files
if [[ ! -d swc ]]; then
   wget https://swcarpentry.github.io/python-novice-inflammation/data/python-novice-inflammation-data.zip
   unzip -j -d swc python-novice-inflammation-data.zip
   rm python-novice-inflammation-data.zip
else
   >&2 echo swc already exists
fi

>&2 echo Done
exit 0

