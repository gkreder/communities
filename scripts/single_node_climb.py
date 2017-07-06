#!/usr/bin/env python
import sys
import os
################################################################################
scripts_dir = os.getcwd()
top_dir = scripts_dir + '/../data/db_cleaned/'
raw_dir = top_dir + 'dmp/raw_mappings/'
mapped_dir = top_dir + 'dmp/clean_mappings/'
ref_dir = top_dir + 'reference_files/'
clean_dir = top_dir + 'fasta_cleaned/'
node_dir = top_dir + 'dmp/nodes/'

index = int(sys.argv[1])
names_file = ref_dir + 'names.dmp'
nodes_file = ref_dir + 'nodes.dmp'
################################################################################
def get_node(name):
    return name.split('\t|\t')[0]

def get_child(node):
    return node.split('\t|\t')[0]

def get_parent(node):
    return node.split('\t|\t')[1]

def climb(current_node, names, nodes):
    found_names = []
    for name in names:
        if get_node(name) == current_node:
            found_names.append(name)

    for node in nodes:
        if get_child(node) == current_node:
            next_node = '\t|\t'.join(node.split('\t|\t')[0 : 3])
            break

    return(found_names, next_node)
################################################################################
mapping_files = [x for x in os.listdir(raw_dir) if x.split('.')[0] != '' and x.split('.') != '..']
lines = []
nodes_fname_out = node_dir + mapping_files[index].replace('out', 'nodes')
names_fname_out = node_dir + mapping_files[index].replace('out', 'names')
with open(raw_dir + mapping_files[index]) as f:
    for line in f:
        lines.append(line.strip())
starting_line_number = int(lines[5])
starting_name = lines[7]
starting_node = get_node(starting_name)

names = []
with open(names_file) as n:
    names_temp = n.readlines()
for line in names_temp:
    names.append(line.strip())

nodes = []
with open(nodes_file) as n:
    nodes_temp = n.readlines()
for line in nodes_temp:
    nodes.append(line.strip())

out_names = []
out_nodes = []
current_node = starting_node
while current_node != '1':
    found_names, next_node = climb(current_node, names, nodes)
    for name in found_names:
        out_names.append(name)
    out_nodes.append(next_node)
    print(next_node)
    current_node = get_parent(next_node)

found_names, next_node = climb(current_node, names, nodes)
for name in found_names:
    out_names.append(name)
out_nodes.append(next_node)

with open(names_fname_out, 'w') as f:
    for name in out_names:
        print(name, file=f)
    f.close()

with open(nodes_fname_out, 'w') as f:
    for node in out_nodes:
        print(node, file=f)
    f.close()
