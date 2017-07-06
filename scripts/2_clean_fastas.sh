#!/bin/bash

rm -r ../data/db_cleaned/fasta_cleaned
mkdir ../data/db_cleaned/fasta_cleaned
python clean_fastas.sh
