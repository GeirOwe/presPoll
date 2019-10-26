import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

polls = pd.read_csv('president_primary_polls.csv')

#print(polls.shape)
#print(polls.dtypes)
#print(polls.describe())
#print(polls.head(10))
#[]

#data for DEM's
dems = polls.loc[polls["party"] == "DEM"]

#data for REP's
reps = polls.loc[polls["party"] == "REP"]

print()
print()

print()
print('------------------------------------')
print('      DEMOCRATS')
print('------------------------------------')
print()


#print likelihood of DEMS beeing elected
stats = dems.groupby(['candidate_name'])['pct'].mean()
statsDem = stats.sort_values(ascending=False)
print(statsDem[:10])

print()
print('------------------------------------')
print('      REPUBLICANS')
print('------------------------------------')
print()
#print likelihood of REPS beeing elected
stats = reps.groupby(['candidate_name'])['pct'].mean()
statsRep = stats.sort_values(ascending=False)
print(statsRep[:10])


#plot candidates likelihood to win
#df = polls.groupby(['candidate_name']).pct.mean()
#df = df.sort_values()
#df.plot(kind = 'bar')
#plt.show()





