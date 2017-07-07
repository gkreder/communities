import sys
import os

scripts_dir = os.getcwd()
top_dir = scripts_dir + '/../data/db_cleaned/'
raw_dir = top_dir + 'dmp/raw_mappings/'
mapped_dir = top_dir + 'dmp/clean_mappings/'
ref_dir = top_dir + 'reference_files/'
clean_dir = top_dir + 'fasta_cleaned/'

# Used to rename all the out files corresponding to the fasta file name
def rename_files():
    map_files = [x for x in os.listdir(raw_dir) if '.DS_Store' not in x]
    os.chdir(raw_dir)
    for fname in map_files:
        with open(fname) as f:
            lines = f.readlines()
        fname_new = ".".join(lines[1].strip().split('.')[ : -1]) + '.out'
        os.rename(fname, fname_new)
    os.chdir(scripts_dir)


# Creates mapping file from sequence identifiers to taxonomy ids
def seqid_taxid_map(fname_out):
    map_files = [x for x in os.listdir(raw_dir) if '.DS_Store' not in x]
    os.chdir(raw_dir)

    pairs = []
    for fname in map_files:
        lines = []
        with open(fname) as f:
            for line in f:
                lines.append(line.strip())
            f.close()
        fasta_fname = lines[1]
        taxid = lines[7].strip().split('\t|\t')[0]
        with open(clean_dir + fasta_fname) as f:
            header_lines = []
            for line in f:
                if line[0] == '>':
                    header_lines.append(line)
            f.close()
        for line in header_lines:
            if '|' in line:
                seqid = '|'.join(line[1 : ].split('|')[0 : 2])
            else:
                seqid = line[1 : ].split(' ')[0]
            pairs.append((seqid, taxid))

    os.chdir(top_dir)
    with open(fname_out, 'w') as f:
        for pair in pairs:
            # print(pair[0].strip() + '\t' + pair[1].strip(), file=f)
            print(pair[0] + '\t' + pair[1], file=f)

    with open('taxids.txt', 'w') as f:
        for pair in pairs:
            print(pair[1], file=f)
    os.chdir(scripts_dir)



rename_files()
seqid_taxid_map("seqid_taxid_map.out")
