#!/bin/bash
if [ $# -eq 0 ]
  then
    echo '''
      Error: Must specify input file
      Example Call: sh 2_clean_report.sh my_report.tsv
    '''
  else
    # centrifuge -q -x ../../data/db_cleaned/db_index ${1/.fastq/_report.tsv} -S ${1/.fastq/_mapping.out}
    echo ${1/.fastq/_mapping.out}
fi
