import os
import sys
# scripts_dir = os.getcwd()
scripts_dir = os.path.dirname(os.path.realpath(__file__))
aux_scripts_dir = scripts_dir + 'aux_scripts/'
processing_scripts_dir = scripts_dir + 'process_results/'
run_centrifuge_dir = scripts_dir + 'process_results/'
cluster_submission_dir = scripts_dir + 'cluster_submission/'
data_dir = scripts_dir + '/../data/'
db_cleaned_dir = data_dir + 'db_cleaned/'
test_reads_dir = data_dir + 'test_reads/'
dmp_dir = db_cleaned_dir + 'dmp/'
Dropout_strain_1 = test_reads_dir + 'Dropout_strain_1/'
names = db_cleaned_dir + 'names.out'
nodes = db_cleaned_dir + 'nodes.out'
seqid_taxid_map = db_cleaned_dir + 'seqid_taxid_map.out'




def get_clean_lines(fname, headers = True):
    with open(fname) as f:
        lines = f.readlines()
        f.close()
    for line_number, line in enumerate(lines):
        lines[line_number] = line.strip()
    if headers:
        lines = lines[1 : ]
        headers = lines[0]
        return lines, headers
    else:
        return lines
