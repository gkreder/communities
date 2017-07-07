#!/bin/bash
rm -r ../../data/db_cleaned/dmp/std_out
rm -r ../../data/db_cleaned/dmp/std_err
rm -r ../../data/db_cleaned/dmp/raw_mappings
rm -r ../../data/db_cleaned/dmp/nodes
mkdir ../../data/db_cleaned/dmp/raw_mappings
mkdir ../../data/db_cleaned/dmp/nodes
# rsync -r -v gkreder@chef.compbio.ucsf.edu:~/Fischbach/communities/data/db_cleaned/dmp/* ../data/db_cleaned/dmp/
sh ../pull_from_server.sh
python ../aux_scripts/mapping.py
sh ../push_to_server.sh
