import sys
import os

scripts_dir = os.getcwd()
top_dir = scripts_dir + '/../data/db_cleaned/'
raw_dir = top_dir + 'dmp/raw_mappings/'
mapped_dir = top_dir + 'dmp/clean_mappings/'
ref_dir = top_dir + 'reference_files/'
clean_dir = top_dir + 'fasta_cleaned/'
node_dir = top_dir + 'dmp/nodes/'

os.chdir(node_dir)

node_files = [x for x in os.listdir() if x.split('.')[0] != '' \
                                      and x.split('.') != '..' \
                                      and '.nodes' in x]

name_files = [x for x in os.listdir() if x.split('.')[0] != '' \
                                      and x.split('.') != '..' \
                                      and '.names' in x]


nodes = set({})
names = set({})

for node_file in node_files:
    with open(node_file) as f:
        for line in f:
            nodes.add(line.strip())

for name_file in name_files:
    with open(name_file) as f:
        for line in f:
            names.add(line.strip())

os.chdir(top_dir)
with open('nodes.out', 'w') as f:
    for node in nodes:
        print(node, file=f)

with open('names.out', 'w') as f:
    for name in names:
        print(name, file=f)
