#!/bin/bash
rm -r ../../data/db_cleaned/dmp/std_out
rm -r ../../data/db_cleaned/dmp/std_err
mkdir ../../data/db_cleaned/dmp/std_out
mkdir ../../data/db_cleaned/dmp/std_err

cd ../cluster_submission
qsub single_node_climb.sh
cd ../build_db
