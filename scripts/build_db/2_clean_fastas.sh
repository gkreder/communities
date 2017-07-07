#!/bin/bash

rm -r ../../data/db_cleaned/fasta_cleaned
mkdir ../../data/db_cleaned/fasta_cleaned
python ../aux_scripts/clean_fastas.py
cat ../../data/db_cleaned/fasta_cleaned/* > ../data/db_cleaned/db_sequences.out
sh ../push_to_server.sh
