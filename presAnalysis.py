import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

#use pandas to read the csv file into a DataFrame
polls = pd.read_csv('president_primary_polls.csv')

#print(polls.dtypes) - the columns names and their data types
#print(polls.describe())
#[]

#data for DEM's
dems = polls.loc[polls["party"] == "DEM"]

#data for REP's
reps = polls.loc[polls["party"] == "REP"]

#get the poll date from start_date (found in column 17 in all rows) - just pick the one from second row
pollDate = str(polls.iloc[1, 17])

print()
print('The poll was done: ' + pollDate)
#print('The size of the dataset: '+ str(polls.shape))
print()
print('------------------------------------')
print('      DEMOCRATS')
print('------------------------------------')
print()
#print likelihood of DEMS beeing elected
stats = dems.groupby(['candidate_name'])['pct'].mean()
statsDem = stats.sort_values(ascending=False)
#print the 20 highest ranked candidates
print(statsDem[:20])

print()
print('------------------------------------')
print('      REPUBLICANS')
print('------------------------------------')
print()
#print likelihood of REPS beeing elected
stats = reps.groupby(['candidate_name'])['pct'].mean()
statsRep = stats.sort_values(ascending=False)

#print the 20 highest ranked candidates
print(statsRep[:20])






