#!/bin/bash
# aparcstats2table for BrainAge prediction
# must run using python2 environment
# conda activate freesurfer6
# edit SUBJECTS_DIR, OUT and subs.txt for the relevant dataset

export SUBJECTS_DIR="/Volumes/PsychiatryNeuroinformatics$/Data/Meaghan_FS/PING/6.0.0"
export OUT=/Users/meaghan/Projects/BrainAge/data/ping_schaefer_aparc

# Schaefer Atlas Parcellation
aparcstats2table --subjectsfile=subs.txt \
--hemi=lh \
--parc Schaefer2018_400Parcels_7Networks_order \
-m area \
-d comma \
--tablefile $OUT/lh_aparc_stats_area.csv

aparcstats2table --subjectsfile=subs.txt \
--hemi=rh \
--parc Schaefer2018_400Parcels_7Networks_order \
-m area \
-d comma \
--tablefile $OUT/rh_aparc_stats_area.csv

aparcstats2table --subjectsfile=subs.txt \
--hemi=lh \
--parc Schaefer2018_400Parcels_7Networks_order \
-m thickness \
-d comma \
--tablefile $OUT/lh_aparc_stats_thickness.csv

aparcstats2table --subjectsfile=subs.txt \
--hemi=rh \
--parc Schaefer2018_400Parcels_7Networks_order \
-m thickness \
-d comma \
--tablefile $OUT/rh_aparc_stats_thickness.csv