## BrainAGE Prediction for ELGAN Data
## Created by Meaghan Perdue
## 03-14-2025
This project tests performance of BrainAGE (age-gap-estimate) prediction models on MRI data acquired from adolescents born very preterm and comparison group of full-term born children/adolescents from the Pediatric Imaging, Neurocognition, and Genetics (PING) cohort participants scanned at UMass Chan Medical School (PING site: UMMS).

Project under development.

## Global BrainAGE model
First set of models test Global-BrainAGE model: <https://centilebrain.org/#/brainAge_global>
Inputs: Freesurfer 6.0.0 D-K parcellation and subcortical segmentation data \
1. Run 'aparc_aseg_all.sh' for D-K cortical parcellation and aseg volume data tables. \
2. Run 'make_data_table.py' to compile parcellation data formatted for BrainAGE template \
3. Upload data to BrainAGE model (males and females separately, select model for age 5-40 years) \
4. Download computed BrainAGE and predicted age output files \
5. Run 'compile_output.py' to prepare BrainAGE estimates for analysis \


## Developmental BrainAGE model
Second set of models test Developmental-BrainAGE model: <https://centilebrain.org/#/brainAge_developmental>
Inputs: Freesurfer 6.0.0 Schaefer parcellation data. \
1. Run 'schaefer_parcellation.sh' to apply Schaefer parcellation to recon-all outputs. Based on code from: <https://github.com/ThomasYeoLab/CBIG/blob/master/stable_projects/brain_parcellation/Schaefer2018_LocalGlobal/Parcellations/project_to_individual/README>. Requires gcs files from: <https://www.dropbox.com/s/1vk6zjus5nogd0z/gcs_Schaefer2018_update20190916.zip?dl=0> \
2. Run 'aparc_stats2table_schaefer.sh' for Schaefer parcellation data across subjects. \
3. Run 'make_data_table_DevBrainAGE.py' to compile parcellation data formatted for Developmental BrainAGE template. \
4. Upload data to Developmental BrainAGE model (males and females separately) \
5. Download computed BrainAGE and predicated age output files \
6. Run 'compile_output.py' to prepare BrainAGE estimates for analysis \