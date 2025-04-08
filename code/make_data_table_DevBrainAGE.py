# Prepare data for BrainAGE estimation via Developmental Brain-AGE model: <https://centilebrain.org/#/brainAge_developmental> 
# Based on Schaefer Atlas
# merges aparc outputs formatted for brainAGE template: LH thickness, RH thickness, LH area, RH area
# Before running this script, do schaefer_parcellation.sh to generate Shaefer Parcellations for each subject
#  then aparc_stats2table_schaefer.sh to generate group-wise stats tables for each metric and hemisphere
# create .csv file in input data folder that contains 2 column with list of subject IDs and ages (males/females in separate files)
# males and females must be run separately
# aparc files must contain SubjectID column that matches brainAGE participant info files (may need to edit if Freesurfer folders are named differently)
# update read and write paths as needed for current dataset
# paste contents into template_DEVbrainage.xlsx and save file for upload to BrainAGE estimator
import pandas as pd

#read participant age 
males=pd.read_csv('/Users/meaghan/Projects/BrainAge/data/elgan_DevBrainAGE_inputs/elgan_males_age.csv')
females=pd.read_csv('/Users/meaghan/Projects/BrainAge/data/elgan_DevBrainAGE_inputs/elgan_females_age.csv')

#read aparc and aseg table outputs from freesurfer
lhthickness=pd.read_csv('/Users/meaghan/Projects/BrainAge/data/elgan_schaefer_aparc/lh_aparc_stats_thickness.csv')
rhthickness=pd.read_csv('/Users/meaghan/Projects/BrainAge/data/elgan_schaefer_aparc/rh_aparc_stats_thickness.csv')
lharea=pd.read_csv('/Users/meaghan/Projects/BrainAge/data/elgan_schaefer_aparc/lh_aparc_stats_area.csv')
rharea=pd.read_csv('/Users/meaghan/Projects/BrainAge/data/elgan_schaefer_aparc/rh_aparc_stats_area.csv')

# rename first column in each sheet to study_id 
lhthickness = lhthickness.rename(columns={lhthickness.columns[0]: 'SubjectID'})
rhthickness = rhthickness.rename(columns={rhthickness.columns[0]: 'tmp'})
lharea = lharea.rename(columns={lharea.columns[0]: 'tmp'})
rharea = rharea.rename(columns={rharea.columns[0]: 'tmp'})

# remove columns not needed for brainAGE template
lhthickness = lhthickness.drop(lhthickness.columns[201:203], axis=1)
rhthickness = rhthickness.drop(rhthickness.columns[201:203], axis=1)
lharea = lharea.drop(lharea.columns[201:204], axis=1)
rharea = rharea.drop(rharea.columns[201:204], axis=1)

# merge all aparc and aseg files into one
dfs = [lhthickness, rhthickness, lharea, rharea]
all = pd.concat(dfs, axis=1)
all = all.drop("tmp", axis=1)
malesdat = pd.merge(males, all, on="SubjectID", how='left')
femalesdat = pd.merge(females, all, on="SubjectID", how='left')

# write outputs to csv
malesdat.to_csv('/Users/meaghan/Projects/BrainAge/data/elgan_DevBrainAGE_inputs/DevbrainAGE_elgan_males_data_FS6.csv', index=False)
femalesdat.to_csv('/Users/meaghan/Projects/BrainAge/data/elgan_DevBrainAGE_inputs/DevbrainAGE_elgan_females_data_FS6.csv', index=False)