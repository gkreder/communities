rm -r ../data/db_cleaned/dmp/std_out
rm -r ../data/db_cleaned/dmp/std_err
rm -r ../data/db_cleaned/dmp/raw_mappings
rm -r ../data/db_cleaned/dmp/nodes
mkdir ../data/db_cleaned/dmp/raw_mappings
mkdir ../data/db_cleaned/dmp/nodes
rsync -r -v gkreder@chef.compbio.ucsf.edu:~/Fischbach/communities/data/db_cleaned/dmp/* ../data/db_cleaned/dmp/
python mapping.py
