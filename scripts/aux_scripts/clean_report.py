import sys
import os

scripts_dir = os.getcwd() + '/..'
top_dir = scripts_dir + '/../data/db_cleaned/'
raw_dir = top_dir + 'dmp/raw_mappings/'
mapped_dir = top_dir + 'dmp/clean_mappings/'
ref_dir = top_dir + 'reference_files/'
clean_dir = top_dir + 'fasta_cleaned/'
node_dir = top_dir + 'dmp/nodes/'


report_fname = sys.argv[1]
seqid_taxid_map = top_dir + 'seqid_taxid_map.out'

with open(seqid_taxid_map) as f:
    seqids = set({})
    for line in f:
        seqid = line.strip().split('\t')[1]
        seqids.add(seqid)

with open(report_fname) as f:
    lines = f.readlines()
    for line_number, line in enumerate(lines):
        lines[line_number] = line.strip()

with open(report_fname.replace('.tsv', '_cleaned.tsv'), 'w') as f:
    for line_number, line in enumerate(lines):
        if line_number == 0:
            print(line, file=f)
            continue
        test_seqid = line.split('\t')[1]
        if test_seqid in seqids:
            print(line, file=f)
        else:
            if line.split('\t')[-1] != '0.0':
                sys.exit('Error: Read mapped to upstream node')
