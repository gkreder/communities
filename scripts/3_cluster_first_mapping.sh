rm -r ../data/db_cleaned/dmp/std_out
rm -r ../data/db_cleaned/dmp/std_err
mkdir ../data/db_cleaned/dmp/std_out
mkdir ../data/db_cleaned/dmp/std_err
cd submission
qsub make_dmp.sh
cd ..