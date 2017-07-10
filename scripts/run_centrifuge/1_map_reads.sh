#!/bin/bash
if [ $# -eq 0 ]
  then
    echo '''
      Error: Must specify input file
      Example Call: sh 1_map_reads.sh my_reads.fastq
    '''
  else
    "centrifuge -q -x ../../data/db_cleaned/db_index --report-file ${1/.fastq/_report.tsv} -S ${1/.fastq/_mapping.out} $1"
    # "centrifuge -q -x ../../data/db_cleaned/db_index $1"
    # "centrifuge -q -x ../../data/db_cleaned/db_index ../../data/test_reads/Dropout strain 1/Day1_S2_L001_R1_001.fastq"
fi
