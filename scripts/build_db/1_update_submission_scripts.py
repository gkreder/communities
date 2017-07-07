#!/usr/bin/env python
import os
import sys
scripts_dir = os.getcwd() + '/..'
submissions_dir = scripts_dir + '/cluster_submission/'
data_dir = scripts_dir + '/../data/'
top_dir = data_dir + 'db_cleaned/'
fasta_dir = top_dir + 'fasta_raw/'


fasta_files = [x for x in os.listdir(fasta_dir) if x.split('.') != '' and x.split('.') != '.']
num_files = len(fasta_files)

os.chdir(submissions_dir)
submission_files = [x for x in os.listdir(submissions_dir) if x.split('.') != '' and x.split('.') != '.']
for s_fname in submission_files:
    with open(s_fname) as f:
        lines = f.readlines()
        f.close()
    for line_number,line in enumerate(lines):
        lines[line_number] = line.strip()

    with open(s_fname, 'w') as f:
        for line in lines:
            if '#$ -t' in line:
                new_line = '#$ -t 1-' + str(num_files)
                print(new_line, file=f)
            else:
                print(line, file=f)
