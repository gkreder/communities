import sys
import os
from fuzzywuzzy import fuzz

scripts_dir = os.getcwd()
top_dir = scripts_dir + '/../data/db_cleaned/'
raw_dir = top_dir + '96 strain FASTA/'
clean_dir = top_dir + 'fasta_cleaned/'
ref_dir = top_dir + 'reference_files/'



# def longest_common_substring(s1, s2):
#    m = [[0] * (1 + len(s2)) for i in range(1 + len(s1))]
#    longest, x_longest = 0, 0
#    for x in range(1, 1 + len(s1)):
#        for y in range(1, 1 + len(s2)):
#            if s1[x - 1] == s2[y - 1]:
#                m[x][y] = m[x - 1][y - 1] + 1
#                if m[x][y] > longest:
#                    longest = m[x][y]
#                    x_longest = x
#            else:
#                m[x][y] = 0
#    return s1[x_longest - longest: x_longest]


names_fname = ref_dir + 'names.dmp'
with open(names_fname) as f:
    lines_raw = f.readlines()
    names_lines = []
    for line in lines_raw:
        names_lines.append(line.strip())

# cleaned_fnames = os.listdir(clean_dir)
# file_index = int(sys.argv[1])
fname = sys.argv[1]
# fname = cleaned_fnames[file_index]
if ".fsa_nt" in fname:
    search_text = " ".join(fname.replace(".fsa_nt", "").split("-")[1 : ])
elif ".fa_txt" in fname:
    # Hard coded
    search_text = "Bacteroides sp. 2_1_22"
elif ".fa_rtfd" in fname:
    search_text = " ".join(fname.replace(".fa_rtfd", "").split("-"))
elif ".fa_rtf" in fname:
    search_text = " ".join(fname.replace(".fa_rtf", "").split("-"))
elif ".fna" in fname:
    search_text = fname.split("genomic")[1][1 : ].replace(".fna", "").replace("-", " ")
else:
    sys.exit("Error: Unrecognized file type - " + fname)
# max_length = 0
max_ratio = 0
found_line_number = -1
found_line = "None"
# names_lines = names_lines[0 : 10000]
for line_number, line in enumerate(names_lines):
    query_text = line.split("|")[1].replace("\t", "")
    # lcs = longest_common_substring(search_text.lower(), query_text.lower())ratio =
    fuzz_ratio = fuzz.ratio(search_text.lower(), query_text.lower())

    # if len(lcs) > max_length:
    if fuzz_ratio > max_ratio:
        max_ratio = fuzz_ratio
        found_line_number = line_number
        found_line = line

print("# File name")
print(fname)
print("# Search Text")
print(search_text)
print("# Line Number")
print(found_line_number)
print("# Found Line")
print(found_line)
