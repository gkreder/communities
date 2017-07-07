#!/bin/bash
sh ../pull_from_server
python ../aux_scripts/merge_node_files.py
centrifuge-build --conversion-table ../../data/db_cleaned/seqid_taxid_map.out --taxonomy-tree ../../data/db_cleaned/nodes.out --name-table ../../data/db_cleaned/names.out ../../data/db_cleaned/db_sequences.out ../../data/db_cleaned/db_index
