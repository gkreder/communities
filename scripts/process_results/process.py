################################################################
# Gabe Reder - 7/2017 - gkreder@gmail.com
################################################################
import sys
import os
sys.path.append('./../../')
from scripts import paths
################################################################
def get_all_species(report_fname):
    lines, headers = paths.get_clean_lines(report_fname)
    species_list = []
    for line_number, line in enumerate(lines):
        species = line.split('\t')[0]
        species_list.append(species)
    return(species_list)

def get_nonzero_species(report_fname):
    lines, headers = paths.get_clean_lines(report_fname)
    species_list = []
    for line_number, line in enumerate(lines):
        species = line.split('\t')[0]
        numreads = int(line.split('\t')[4])
        numunique = float(line.split('\t')[5])
        abundance = float(line.split('\t')[6])
        if numreads != 0.0:
            species_list.append(species)

    return species_list


def get_nonzero_taxids(report_fname):
    lines, headers = paths.get_clean_lines(report_fname)
    taxids = []
    for line_number, line in enumerate(lines):
        taxid = line.split('\t')[1]
        species = line.split('\t')[0]
        numreads = int(line.split('\t')[4])
        numunique = float(line.split('\t')[5])
        abundance = float(line.split('\t')[6])
        if numreads != 0.0:
            taxids.append(taxid)
    return taxids

def get_child_taxids():
    """
    Meant to retrieve only childless nodes in the target db taxonomy
    """
    lines = paths.get_clean_lines(paths.seqid_taxid_map, headers = False)
    taxids = set([])
    for line in lines:
        taxids.add(line.split('\t')[1])
    return list(taxids)

def get_upstream_taxids():
    """
    Retrieves only the upstream taxids (nodes that are not in the 96 species)
    """
    lines = paths.get_clean_lines(paths.names, headers = False)
    taxids = set([])
    for line in lines:
        taxids.add(line.split('\t|\t')[0])

    return(list(taxids))

report = paths.Dropout_strain_1 + 'Day1_S2_L001_k_report.tsv'
result_taxids = get_nonzero_taxids(report)
child_taxids = get_child_taxids()
upstream_taxids = get_upstream_taxids()
