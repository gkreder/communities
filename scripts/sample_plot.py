import sys
import os
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns


scripts_dir = os.getcwd()
top_dir = scripts_dir + '/../data/db_cleaned/'
raw_dir = top_dir + 'dmp/raw_mappings/'
mapped_dir = top_dir + 'dmp/clean_mappings/'
ref_dir = top_dir + 'reference_files/'
clean_dir = top_dir + 'fasta_cleaned/'
node_dir = top_dir + 'dmp/nodes/'
data_dir = scripts_dir + '/../data/'
reads_dir = data_dir + 'test_reads/'




complete_fname = reads_dir + 'centrifuge_report_cleaned.tsv'
dropout_fname = reads_dir + 'Dropout_strain_1/Day1_S2_L001_R1_001_report_cleaned.tsv'

complete_reads = {}
dropout_reads = {}
index = {}
x = []

with open(complete_fname) as f:
    for line_number,line in enumerate(f):
        if line_number == 0:
            continue
        species_name = line.strip().split('\t')[0]
        abundance = line.strip().split('\t')[-1]
        abundance = float(abundance)
        complete_reads[species_name] = abundance

with open(dropout_fname) as f:
    for line_number,line in enumerate(f):
        if line_number == 0:
            continue
        species_name = line.strip().split('\t')[0]
        abundance = float(line.strip().split('\t')[-1])
        dropout_reads[species_name] = abundance

for species in complete_reads:
    if(species) not in dropout_reads:
        dropout_reads[species] = 0.0

for i, species in enumerate(complete_reads):
    index[i] = species

# keylist = complete_reads.keys()
# keylist.sort()
complete_hist = []
dropout_hist = []
for key in sorted(complete_reads.keys()):
    complete_hist.append(complete_reads[key])
    dropout_hist.append(dropout_reads[key])



w = 0.3
centers = range(len(complete_reads))
centers_shifted = [c + w for c in centers]
print(centers)

ax = plt.subplot(111)

# ax.bar(centers-w, y,width=w,color='b',align='center')
ax.bar(centers, complete_hist,width=w,color='g',align='center')
ax.bar(centers+w, dropout_hist,width=w,color='r',align='center')
ax.autoscale(tight=True)
plt.show()

# plt.bar(centers, complete_reads.values(), align='center')
# plt.bar(centers, complete_hist, align='center')
# plt.show()

# plt.hist([complete_hist, dropout_hist], color=['r','b'], alpha=0.5, bins= len(dropout_hist) + 1)
# plt.show()
