# Compile BrainAGE outputs into database for analysis
import pandas as pd

# Read compiled data with freesurfer aparc and aseg values
maledat=pd.read_csv('/Users/meaghan/Projects/BrainAge/data/brainAGE_elgan_males_data.csv')
femaledat=pd.read_csv('/Users/meaghan/Projects/BrainAge/data/brainAGE_elgan_females_data.csv')

# Read brainAGE outputs
##males
maleBrainAge=pd.read_csv('/Users/meaghan/Projects/BrainAge/results/output_file_2025-03-13-19-36-01_BrainAGE_male.csv')
maleBrainAgeAdj=pd.read_csv('/Users/meaghan/Projects/BrainAge/results/output_file_2025-03-13-19-36-01_Adjusted_BrainAGE_male.csv')
malePredAge=pd.read_csv('/Users/meaghan/Projects/BrainAge/results/output_file_2025-03-13-19-36-01_MR_predicted_age_male.csv')
malePredAgeAdj=pd.read_csv('/Users/meaghan/Projects/BrainAge/results/output_file_2025-03-13-19-36-01_Adjusted_MR_predicted_age_male.csv')

##females
femaleBrainAge=pd.read_csv('/Users/meaghan/Projects/BrainAge/results/output_file_2025-03-13-19-46-01_BrainAGE_female.csv')
femaleBrainAgeAdj=pd.read_csv('/Users/meaghan/Projects/BrainAge/results/output_file_2025-03-13-19-46-01_Adjusted_BrainAGE_female.csv')
femalePredAge=pd.read_csv('/Users/meaghan/Projects/BrainAge/results/output_file_2025-03-13-19-46-01_MR_predicted_age_female.csv')
femalePredAgeAdj=pd.read_csv('/Users/meaghan/Projects/BrainAge/results/output_file_2025-03-13-19-46-01_Adjusted_MR_predicted_age_female.csv')

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
all_out.to_csv('/Users/meaghan/Projects/BrainAge/results/elgan_brainAGE_outputs_20250314.csv', index=False)
