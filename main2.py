#this programme reads a poll statistics on the US Election 2020 and rankes the candidates with most votes

from flask import Flask, render_template
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# __name__ means this current file. In this case, it will be newMain.py.
# This current file will represent my web application.
app = Flask(__name__)

#reading the CSV file
def DEM(polls):
    #data for DEM's
    #print(type(polls))
    dems = polls.loc[polls["party"] == "DEM"]
    #print(type(dems))
    #sort likelihood of DEMS candidates beeing elected
    #print(dems.dtypes)
    #print(dems['candidate_name'])
    #print(dems.shape)
    #stats = dems.groupby(['candidate_name'])['pct'].mean()
    stats = dems.groupby('candidate_name')['pct'].mean()
    #print(type(stats))
    #print(stats)
    statsDem = stats.sort_values(ascending=False)
    #print(type(statsDem))
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
#print(type(statsDem))
#convert from pandas series to pandas dataframe to be able to access the elements
dfDem = statsDem.to_frame()
#print(type(dfDem))
#print(dfDem)
#print(dfDem.dtypes)
xName = str(dfDem.iloc[0:1,0:1]).strip('pct\ncandidate_name ')
print(xName)
xName = str(dfDem.iloc[1:2,0:1]).strip('pct ')
print(xName)

#REPULICANS
statsRep = REP(polls)
#convert from pandas series to pandas dataframe to be able to access the elements
dfRep = statsRep.to_frame()


      
#the starting page: ./
@app.route('/')
@app.route('/dems')
def dems():
    user = {'username': 'Democrats'}
    posts = [
        {'candidate': str(dfDem.iloc[0:1,0:1]).strip('pct\ncandidate_name ')},
        {'candidate': str(dfDem.iloc[1:2,0:1]).strip('pct\ncandidate_name  ')},
        {'candidate': str(dfDem.iloc[2:3,0:1]).strip('pct\ncandidate_name  ')},
        {'candidate': str(dfDem.iloc[3:4,0:1]).strip('pct\ncandidate_name  ')},
        {'candidate': str(dfDem.iloc[4:5,0:1]).strip('pct\ncandidate_name  ')},
        {'candidate': str(dfDem.iloc[5:6,0:1]).strip('pct\ncandidate_name  ')}
    ]
    return render_template('dems.html', title='Home', user=user, posts=posts)

#the page for the REPublicans
@app.route('/reps')
def reps():
    user = {'username': 'Republicans'}
    posts = [
        {'candidate': str(dfRep.iloc[0:1,0:1]).strip('pct\ncandidate_name  ')},
        {'candidate': str(dfRep.iloc[1:2,0:1]).strip('pct\ncandidate_name  ')},
        {'candidate': str(dfRep.iloc[2:3,0:1]).strip('pct\ncandidate_name  ')},
        {'candidate': str(dfRep.iloc[3:4,0:1]).strip('pct\ncandidate_name  ')},
        {'candidate': str(dfRep.iloc[4:5,0:1]).strip('pct\ncandidate_name  ')},
        {'candidate': str(dfRep.iloc[5:6,0:1]).strip('pct\ncandidate_name  ')}
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







