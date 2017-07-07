import os
import sys
import shutil

scripts_dir = os.getcwd()
top_dir = scripts_dir + '/../data/db_cleaned/'
raw_dir = top_dir + '96 strain FASTA/'
clean_dir = top_dir + 'fasta_cleaned/'
ref_dir = top_dir + 'reference_files/'
os.chdir(raw_dir)

raw_fnames = os.listdir()

def parse_file(fname, fname_out, ftype):
    if ftype == ".fsa_nt" or ftype == ".fna" or ftype == ".txt":
        shutil.copyfile(raw_dir + fname, clean_dir + fname_out)
    elif ftype == ".rtf":
        with open(raw_dir + fname) as f:
            lines = f.readlines()
            f.close()
        for line_number, line in enumerate(lines):
            line = line.strip()
            if '>' in line:
                start_line_number = line_number
                break
        if len(line.strip().split(">")) < 2:
            sys.exit("Error in file " + fname + ": missing '>' character")
        with open(clean_dir + fname_out, 'w') as f:
            print(">"+line.strip().split(">")[1].replace("\\", ""), file=f)
            for line_number, line in enumerate(lines):
                if line_number <= start_line_number:
                    continue
                print(line.strip().replace("\\", "").replace("}", "").replace("{", ""), file=f)
            f.close()
    elif ftype == ".rtfd":
        with open(raw_dir + fname + "/TXT.rtf" ) as f:
            lines = f.readlines()
            f.close()
        for line_number, line in enumerate(lines):
            line = line.strip()
            if '>' in line:
                start_line_number = line_number
                break
        if len(line.strip().split(">")) < 2:
            sys.exit("Error in file " + fname + ": missing '>' character")
        with open(clean_dir + fname_out, 'w') as f:
            print(">"+line.strip().split(">")[1].replace("\\", ""), file=f)
            for line_number, line in enumerate(lines):
                if line_number <= start_line_number:
                    continue
                print(line.strip().replace("\\", "").replace("}", "").replace("{", ""), file=f)
            f.close()

for fname in raw_fnames:
    if ".fsa_nt" in fname:
        split = fname.split(".fsa_nt")[0 : -1]
        split = [x.replace(" ", "-") for x in split]
        fname_out = ''.join(split) + ".fsa_nt"
        parse_file(fname, fname_out, ".fsa_nt")
    elif ".fna" in fname:
        split = fname.split(".fna")[0 : -1]
        split = [x.replace(" ", "-") for x in split]
        fname_out = ''.join(split) + ".fna"
        parse_file(fname, fname_out, ".fna")
    elif ".rtfd" in fname:
        fname_out = fname.replace(" ", "-").replace(".rtfd",".fa_rtfd")
        parse_file(fname, fname_out, ".rtfd")
    elif ".rtf" in fname:
        fname_out = fname.replace(" ", "-").replace(".rtf",".fa_rtf")
        parse_file(fname, fname_out, ".rtf")
    elif ".txt" in fname:
        fname_out = fname.replace(" ", "-").replace(".txt",".fa_txt")
        parse_file(fname, fname_out, ".txt")
    else:
        if ".DS_Store" not in fname:
            sys.exit("Error: Unrecognized file type - " + fname)
