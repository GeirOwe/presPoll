import requests

download_url = "https://projects.fivethirtyeight.com/polls-page/president_primary_polls.csv"
#download_url = "https://projects.fivethirtyeight.com/polls-page/president_polls.csv"
target_csv_path = "president_primary_polls.csv"
#target_csv_path = "president_polls.csv"

response = requests.get(download_url)
response.raise_for_status()    # Check that the request was successful
with open(target_csv_path, "wb") as f:
    f.write(response.content)

print("Download ready.")

#validate file using pandas
#import pandas as pd
#use pandas to read the csv file into a DataFrame
#polls = pd.read_csv('president_primary_polls.csv')
#print(polls.dtypes) # the columns names and their data types
#print(polls.describe())