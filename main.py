#this programme reads a poll statistics on the US Election 2020 and rankes the candidates with most votes

from flask import Flask, render_template
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
from datetime import datetime

# __name__ means this current file. In this case, it will be newMain.py.
# This current file will represent my web application.
app = Flask(__name__)

#reading the CSV file
def DEM(polls):
    #data for DEM's
    dems = polls.loc[polls["party"] == "DEM"]
    #sort likelihood of DEMS candidates beeing elected
    stats = dems.groupby(['candidate_name'])['pct'].mean()
    statsDem = stats.sort_values(ascending=False)
    return statsDem

#reading the CSV file
def REP(polls):
    #data for REP's
    reps = polls.loc[polls["party"] == "REP"]
    #sort the REPS candidates according to votes
    stats = reps.groupby(['candidate_name'])['pct'].mean()
    statsRep = stats.sort_values(ascending=False)
    return statsRep

# ----------------------------------------
#start of the main part of the programme
# ----------------------------------------

#use pandas to read the csv file into a DataFrame
polls = pd.read_csv('data/president_primary_polls.csv', low_memory=False)
#print(polls.dtypes) # the columns names and their data types
#print(polls.describe())

#for test purposes
print('')
print('starting ....')

#DEMOCRATS
statsDem = DEM(polls)
#convert from pandas series to pandas dataframe to be able to access the elements
dfDem = statsDem.to_frame()

#retrieve first DEM candidate
#remove the initial column references
xName = str(dfDem.iloc[0:1,0:1]).strip('pct\ncandidate_name ')
# Splitting text and number in string  
dem1Pct = re.findall("\d+\.\d+", xName)[0] #d refers to any number and we include decimals
dem1Name = xName.strip(dem1Pct) #remove the pct from the string and keep name
dem1Pct = re.findall("\d+\.\d", xName)[0] #d refers to any number and we include decimals
print('Name: ', str(dem1Name))
print('Percent: ', str(dem1Pct))

#retrieve second DEM candidate
#remove the initial column references
xName = str(dfDem.iloc[1:2,0:1]).strip('pct\ncandidate_name ')
# Splitting text and number in string  
dem2Pct = re.findall("\d+\.\d+", xName)[0] #d refers to any number and we include all decimals thru d+
dem2Name = xName.strip(dem2Pct) #remove the pct from the string and keep name
dem2Pct = re.findall("\d+\.\d", xName)[0] #d refers to any number and we include only one decimal by removing the +
print('Name: ', str(dem2Name))
print('Percent: ', str(dem2Pct))

#REPUBLICANS
statsRep = REP(polls)
#convert from pandas series to pandas dataframe to be able to access the elements
dfRep = statsRep.to_frame()

#retrieve first REP candidate
#remove the initial column reerences
xName = str(dfRep.iloc[0:1,0:1]).strip('pct\ncandidate_name ')
# Splitting text and number in string  
rep1Pct = re.findall("\d+\.\d+", xName)[0] #d refers to any number and we include decimals
rep1Name = xName.strip(rep1Pct) #remove the pct from the string and keep name
rep1Pct = re.findall("\d+\.\d", xName)[0] #d refers to any number and we include decimals
print('Name: ', str(rep1Name))
print('Percent: ', str(rep1Pct))

#retrieve second REP candidate
#remove the initial column reerences
xName = str(dfRep.iloc[1:2,0:1]).strip('pct\ncandidate_name ')


# Splitting text and number in string  
rep2Pct = re.findall("\d+\.\d+", xName)[0] #d refers to any number and we include all decimals thru d+
rep2Name = xName.strip(rep2Pct) #remove the pct from the string and keep name
rep2Pct = re.findall("\d+\.\d", xName)[0] #d refers to any number and we include only one decimal by removing the +
print('Name: ', str(rep2Name))
print('Percent: ', str(rep2Pct))
      
#the starting page: ./
@app.route('/')
@app.route('/dems')
def dems():
    user = {'username': 'Democrats'}
    posts = [
        {'candidate': str(dem1Name) + ' - ' +str(dem1Pct) + '%'},
        {'candidate': str(dem2Name) + ' - ' +str(dem2Pct) + '%'}
    ]
    return render_template('dems.html', title='Home', user=user, posts=posts)

#the page for the REPublicans
@app.route('/reps')
def reps():
    user = {'username': 'Republicans'}
    posts = [
        {'candidate': str(rep1Name) + ' - ' +str(rep1Pct) + '%'},
        {'candidate': str(rep2Name) + ' - ' +str(rep2Pct) + '%'}
    ]
    return render_template('reps.html', title='Home', user=user, posts=posts)

@app.route("/")
def home():
    return render_template("home.html")

#another page page: ./about
@app.route("/about")
def about():
    return render_template("about.html")

#Having debug=True allows possible Python errors to appear on the web page. This will help us trace the errors.   
# app.run(debug=True)
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

# to run it:
# In your Terminal or Command Prompt go to the folder that contains your main.py.
# Then do py main.py or python main.py. In your terminal or command prompt you should see this output.
#
# Running on http://127.0.0.1:5000/
#
#To deploy our web application to azure:
#https://medium.com/@nikovrdoljak/deploy-your-flask-app-on-azure-in-3-easy-steps-b2fe388a589e







