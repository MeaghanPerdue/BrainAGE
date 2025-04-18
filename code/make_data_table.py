# Prepare data for BrainAGE estimation via Global Brain-AGE model: <https://centilebrain.org/#/brainAge_global> 
# merge aparc and aseg outputs formatted for brainAGE template
# males and females must be run separately
# aparc and aseg files must contain SubjectID column that matches brainAGE participant info files (may need to edit if Freesurfer folders are named differently)
# update read and write paths as needed for current dataset
# check output and save in .xlsx folder for upload to BrainAGE estimator
import pandas as pd

#read participant info (rows 1:6 in brainAGE template)
males=pd.read_csv('/Users/meaghan/Projects/BrainAge/data/ping_brainAGE_Global_inputs/brainAGE_ping_males.csv')
females=pd.read_csv('/Users/meaghan/Projects/BrainAge/data/ping_brainAGE_Global_inputs/brainAGE_ping_females.csv')

#read aparc and aseg table outputs from freesurfer
lhthickness=pd.read_csv('/Users/meaghan/Projects/BrainAge/data/ping_aparc_aseg_out_FS6/lh_aparc_stats_thickness.csv')
rhthickness=pd.read_csv('/Users/meaghan/Projects/BrainAge/data/ping_aparc_aseg_out_FS6/rh_aparc_stats_thickness.csv')
lharea=pd.read_csv('/Users/meaghan/Projects/BrainAge/data/ping_aparc_aseg_out_FS6/lh_aparc_stats_area.csv')
rharea=pd.read_csv('/Users/meaghan/Projects/BrainAge/data/ping_aparc_aseg_out_FS6/rh_aparc_stats_area.csv')
volume=pd.read_csv('/Users/meaghan/Projects/BrainAge/data/ping_aparc_aseg_out_FS6/aseg_stats_vol.csv')

# rename first column in each sheet to study_id 
lhthickness = lhthickness.rename(columns={lhthickness.columns[0]: 'SubjectID'})
rhthickness = rhthickness.rename(columns={rhthickness.columns[0]: 'tmp'})
lharea = lharea.rename(columns={lharea.columns[0]: 'tmp'})
rharea = rharea.rename(columns={rharea.columns[0]: 'tmp'})
volume = volume.rename(columns={volume.columns[0]: 'tmp'})

# remove columns not needed for brainAGE template
lhthickness = lhthickness.drop(lhthickness.columns[35:38], axis=1)
rhthickness = rhthickness.drop(rhthickness.columns[35:38], axis=1)
lharea = lharea.drop(lharea.columns[35:38], axis=1)
rharea = rharea.drop(rharea.columns[35:38], axis=1)

# select aseg volume columns needed for brainAGE template
cols = ["Left-Thalamus-Proper", "Right-Thalamus-Proper", "Left-Caudate", "Right-Caudate", "Left-Putamen", "Right-Putamen", "Left-Pallidum", "Right-Pallidum", "Left-Hippocampus", "Right-Hippocampus", "Left-Amygdala", "Right-Amygdala", "Left-Accumbens-area", "Right-Accumbens-area"]
volume = volume[cols]

# merge all aparg and aseg files into one
dfs = [lhthickness, rhthickness, lharea, rharea, volume]
all = pd.concat(dfs, axis=1)
all = all.drop("tmp", axis=1)
malesdat = pd.merge(males, all, on="SubjectID", how='left')
femalesdat = pd.merge(females, all, on="SubjectID", how='left')

# rename columns to match BrainAge template
cols2 = ["SITE", "SubjectID", "age", "sex", "ScannerType", "FreeSurfer_Version", "L_bankssts_thickavg", "L_caudalanteriorcingulate_thickavg", "L_caudalmiddlefrontal_thickavg", "L_cuneus_thickavg", "L_entorhil_thickavg", "L_fusiform_thickavg", "L_inferiorparietal_thickavg", "L_inferiortemporal_thickavg", "L_isthmuscingulate_thickavg", "L_lateraloccipital_thickavg", "L_lateralorbitofrontal_thickavg", "L_lingual_thickavg", "L_medialorbitofrontal_thickavg", "L_middletemporal_thickavg", "L_parahippocampal_thickavg", "L_paracentral_thickavg", "L_parsopercularis_thickavg", "L_parsorbitalis_thickavg", "L_parstriangularis_thickavg", "L_pericalcarine_thickavg", "L_postcentral_thickavg", "L_posteriorcingulate_thickavg", "L_precentral_thickavg", "L_precuneus_thickavg", "L_rostralanteriorcingulate_thickavg", "L_rostralmiddlefrontal_thickavg", "L_superiorfrontal_thickavg", "L_superiorparietal_thickavg", "L_superiortemporal_thickavg", "L_supramargil_thickavg", "L_frontalpole_thickavg", "L_temporalpole_thickavg", "L_transversetemporal_thickavg", "L_insula_thickavg", "R_bankssts_thickavg", "R_caudalanteriorcingulate_thickavg", "R_caudalmiddlefrontal_thickavg", "R_cuneus_thickavg", "R_entorhil_thickavg", "R_fusiform_thickavg", "R_inferiorparietal_thickavg", "R_inferiortemporal_thickavg", "R_isthmuscingulate_thickavg", "R_lateraloccipital_thickavg", "R_lateralorbitofrontal_thickavg", "R_lingual_thickavg", "R_medialorbitofrontal_thickavg", "R_middletemporal_thickavg", "R_parahippocampal_thickavg", "R_paracentral_thickavg", "R_parsopercularis_thickavg", "R_parsorbitalis_thickavg", "R_parstriangularis_thickavg", "R_pericalcarine_thickavg", "R_postcentral_thickavg", "R_posteriorcingulate_thickavg", "R_precentral_thickavg", "R_precuneus_thickavg", "R_rostralanteriorcingulate_thickavg", "R_rostralmiddlefrontal_thickavg", "R_superiorfrontal_thickavg", "R_superiorparietal_thickavg", "R_superiortemporal_thickavg", "R_supramargil_thickavg", "R_frontalpole_thickavg", "R_temporalpole_thickavg", "R_transversetemporal_thickavg", "R_insula_thickavg", "L_bankssts_surfavg", "L_caudalanteriorcingulate_surfavg", "L_caudalmiddlefrontal_surfavg", "L_cuneus_surfavg", "L_entorhil_surfavg", "L_fusiform_surfavg", "L_inferiorparietal_surfavg", "L_inferiortemporal_surfavg", "L_isthmuscingulate_surfavg", "L_lateraloccipital_surfavg", "L_lateralorbitofrontal_surfavg", "L_lingual_surfavg", "L_medialorbitofrontal_surfavg", "L_middletemporal_surfavg", "L_parahippocampal_surfavg", "L_paracentral_surfavg", "L_parsopercularis_surfavg", "L_parsorbitalis_surfavg", "L_parstriangularis_surfavg", "L_pericalcarine_surfavg", "L_postcentral_surfavg", "L_posteriorcingulate_surfavg", "L_precentral_surfavg", "L_precuneus_surfavg", "L_rostralanteriorcingulate_surfavg", "L_rostralmiddlefrontal_surfavg", "L_superiorfrontal_surfavg", "L_superiorparietal_surfavg", "L_superiortemporal_surfavg", "L_supramargil_surfavg", "L_frontalpole_surfavg", "L_temporalpole_surfavg", "L_transversetemporal_surfavg", "L_insula_surfavg", "R_bankssts_surfavg", "R_caudalanteriorcingulate_surfavg", "R_caudalmiddlefrontal_surfavg", "R_cuneus_surfavg", "R_entorhil_surfavg", "R_fusiform_surfavg", "R_inferiorparietal_surfavg", "R_inferiortemporal_surfavg", "R_isthmuscingulate_surfavg", "R_lateraloccipital_surfavg", "R_lateralorbitofrontal_surfavg", "R_lingual_surfavg", "R_medialorbitofrontal_surfavg", "R_middletemporal_surfavg", "R_parahippocampal_surfavg", "R_paracentral_surfavg", "R_parsopercularis_surfavg", "R_parsorbitalis_surfavg", "R_parstriangularis_surfavg", "R_pericalcarine_surfavg", "R_postcentral_surfavg", "R_posteriorcingulate_surfavg", "R_precentral_surfavg", "R_precuneus_surfavg", "R_rostralanteriorcingulate_surfavg", "R_rostralmiddlefrontal_surfavg", "R_superiorfrontal_surfavg", "R_superiorparietal_surfavg", "R_superiortemporal_surfavg", "R_supramargil_surfavg", "R_frontalpole_surfavg", "R_temporalpole_surfavg", "R_transversetemporal_surfavg", "R_insula_surfavg", "Lthal", "Rthal", "Lcaud", "Rcaud", "Lput", "Rput", "Lpal", "Rpal", "Lhippo", "Rhippo", "Lamyg", "Ramyg", "Laccumb", "Raccumb"] 
malesdat.columns=cols2
femalesdat.columns=cols2

# write outputs to csv
malesdat.to_csv('/Users/meaghan/Projects/BrainAge/data/ping_brainAGE_Global_inputs/brainAGE_ping_males_data_FS6.csv', index=False)
femalesdat.to_csv('/Users/meaghan/Projects/BrainAge/data/ping_brainAGE_Global_inputs/brainAGE_ping_females_data_FS6.csv', index=False)