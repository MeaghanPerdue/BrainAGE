# Compile BrainAGE outputs into database for analysis
# BrainAGE outputs are downloaded as separate .csv files
# point paths to the outputs and pull into a data file for analysis
import pandas as pd

# Read compiled data with freesurfer aparc and aseg values
maledat=pd.read_csv('/Users/meaghan/Projects/BrainAge/data/ping_brainAGE_Global_inputs/brainAGE_ping_males_data_FS6.csv')
femaledat=pd.read_csv('/Users/meaghan/Projects/BrainAge/data/ping_brainAGE_Global_inputs/brainAGE_ping_females_data_FS6.csv')

# Read brainAGE outputs
##males
maleBrainAge=pd.read_csv('/Users/meaghan/Downloads/output_file_2025-03-26-16-32-47_BrainAGE_male.csv')
maleBrainAgeAdj=pd.read_csv('/Users/meaghan/Downloads/output_file_2025-03-26-16-32-47_Adjusted_BrainAGE_male.csv')
malePredAge=pd.read_csv('/Users/meaghan/Downloads/output_file_2025-03-26-16-32-47_MR_predicted_age_male.csv')
malePredAgeAdj=pd.read_csv('/Users/meaghan/Downloads/output_file_2025-03-26-16-32-47_Adjusted_MR_predicted_age_male.csv')

##females
femaleBrainAge=pd.read_csv('/Users/meaghan/Downloads/output_file_2025-03-26-16-29-21_BrainAGE_female.csv')
femaleBrainAgeAdj=pd.read_csv('/Users/meaghan/Downloads/output_file_2025-03-26-16-29-21_Adjusted_BrainAGE_female.csv')
femalePredAge=pd.read_csv('/Users/meaghan/Downloads/output_file_2025-03-26-16-29-21_MR_predicted_age_female.csv')
femalePredAgeAdj=pd.read_csv('/Users/meaghan/Downloads/output_file_2025-03-26-16-29-21_Adjusted_MR_predicted_age_female.csv')

# Rename brainAGE output variables
##males
maleBrainAge = maleBrainAge.rename(columns={maleBrainAge.columns[1]: 'brainage_dif'})
maleBrainAgeAdj = maleBrainAgeAdj.rename(columns={maleBrainAgeAdj.columns[1]: 'brainage_dif_adj'})
malePredAge = malePredAge.rename(columns={malePredAge.columns[1]: 'predicted_age'})
malePredAgeAdj = malePredAgeAdj.rename(columns={malePredAgeAdj.columns[1]: 'predicted_age_adj'})

##females
femaleBrainAge = femaleBrainAge.rename(columns={femaleBrainAge.columns[1]: 'brainage_dif'})
femaleBrainAgeAdj = femaleBrainAgeAdj.rename(columns={femaleBrainAgeAdj.columns[1]: 'brainage_dif_adj'})
femalePredAge = femalePredAge.rename(columns={femalePredAge.columns[1]: 'predicted_age'})
femalePredAgeAdj = femalePredAgeAdj.rename(columns={femalePredAgeAdj.columns[1]: 'predicted_age_adj'})

# Merge brainAGE outputs
##males
dfs_males = [maledat, maleBrainAge, maleBrainAgeAdj, malePredAge, malePredAgeAdj]
male_out = pd.concat(dfs_males, axis=1)
male_out = male_out.drop("Unnamed: 0", axis=1)

##females
dfs_females = [femaledat, femaleBrainAge, femaleBrainAgeAdj, femalePredAge, femalePredAgeAdj]
female_out = pd.concat(dfs_females, axis=1)
female_out = female_out.drop("Unnamed: 0", axis=1)

# Combine male and female outputs into one database
all_out = male_out.append(female_out)

# Write to .csv
all_out.to_csv('/Users/meaghan/Projects/BrainAge/results/ping_brainAGE_Global_outputs/ping_FS6_brainAGE_outputs_20250326.csv', index=False)
