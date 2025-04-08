#!/bin/bash
# create Schaefer Atlas brain parcellation for Developmental BrainAGE prediction
# calculate surface statistics for Schaefer Atlas ROIs
# code derived from <https://github.com/ThomasYeoLab/CBIG/blob/master/stable_projects/brain_parcellation/Schaefer2018_LocalGlobal/Parcellations/project_to_individual/README.md>
# to run for a single subject, do sh schaefer_parcellation.sh SUBJECT_ID
# to run a loop, run sh loop_schaefer_parcellation.sh

# First, symbolic link fsaverage directory to subjects dir (only need to do this once)
#ln -s $FREESURFER_HOME/subjects/fsaverage /Users/meaghan/Projects/BrainAge/subjects

#export SUBJECTS_DIR=/Users/meaghan/Projects/BrainAge/subjects
export SUBJECTS_DIR="/Volumes/PsychiatryNeuroinformatics$/Data/Meaghan_FS/PING/6.0.0"


  mris_ca_label ${1} lh lh.sphere.reg \
    schaefer_gcs_files/lh.Schaefer2018_400Parcels_7Networks.gcs \
    lh.Schaefer2018_400Parcels_7Networks_order.annot

  mris_ca_label ${1} rh rh.sphere.reg \
    schaefer_gcs_files/rh.Schaefer2018_400Parcels_7Networks.gcs \
    rh.Schaefer2018_400Parcels_7Networks_order.annot

  mris_anatomical_stats \
    -f $SUBJECTS_DIR/${1}/stats/lh.Schaefer2018_400Parcels_7Networks_order.stats \
    -b -a $SUBJECTS_DIR/${1}/label/lh.Schaefer2018_400Parcels_7Networks_order.annot \
    ${1} lh

  mris_anatomical_stats \
    -f $SUBJECTS_DIR/${1}/stats/rh.Schaefer2018_400Parcels_7Networks_order.stats \
    -b -a $SUBJECTS_DIR/${1}/label/rh.Schaefer2018_400Parcels_7Networks_order.annot \
    ${1} rh
   
