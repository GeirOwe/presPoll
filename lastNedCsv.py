import requests

download_url = "https://projects.fivethirtyeight.com/polls-page/president_primary_polls.csv"
target_csv_path = "data/president_primary_polls.csv"

response = requests.get(download_url)
response.raise_for_status()    # Check that the request was successful
with open(target_csv_path, "wb") as f:
    f.write(response.content)

print("Download ready.")
