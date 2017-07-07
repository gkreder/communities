#!/bin/bash

#$ -S /bin/bash
#$ -cwd
#$ -r y
#$ -j y
#$ -l mem_free=8G
#$ -o /netapp/home/gkreder/Fischbach/communities/data/db_cleaned/dmp/std_out
#$ -e /netapp/home/gkreder/Fischbach/communities/data/db_cleaned/dmp/std_err
#$ -l arch=linux-x64
#$ -l netapp=8G,scratch=8G
#$ -l h_rt=48:00:00
#$ -t 1-97

source activate centrifuge
cd ../../data/db_cleaned/fasta_cleaned
array=(*)
index=$(($SGE_TASK_ID-1))
cd ..
python -W ignore make_dmp.py ${array[$index]}
