#!/bin/bash
# aparcstats2table for BrainAge prediction
# must run using python2 environment
# conda activate freesurfer6

export SUBJECTS_DIR=/Users/meaghan/Projects/BrainAge/subjects
export OUT=/Users/meaghan/Projects/BrainAge/data


aparcstats2table --subjectsfile=subs.txt \
--hemi=lh \
-m area \
-d comma \
--tablefile $OUT/lh_aparc_stats_area.csv

aparcstats2table --subjectsfile=subs.txt \
--hemi=rh \
-m area \
-d comma \
--tablefile $OUT/rh_aparc_stats_area.csv

aparcstats2table --subjectsfile=subs.txt \
--hemi=lh \
-m thickness \
-d comma \
--tablefile $OUT/lh_aparc_stats_thickness.csv

aparcstats2table --subjectsfile=subs.txt \
--hemi=rh \
-m thickness \
-d comma \
--tablefile $OUT/rh_aparc_stats_thickness.csv

asegstats2table --subjectsfile=subs.txt \
--meas volume \
-d comma \
--tablefile $OUT/aseg_stats_vol.csv

#python make_data_table.py
