import requests
from bs4 import BeautifulSoup
import csv

request_url = "https://www.nba.com/stats"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    'Accept-Language': 'en-US,en;q=0.9',
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
    , }

songs = requests.get(request_url, headers=headers)
songs.raise_for_status()
data = songs.text

soup = BeautifulSoup(data, "html.parser")

#date of result
date = soup.find(class_="LeaderBoardWithButtons_lbwbDate__gsMEu").text
# Find all tables with the specific class
check = soup.find('div', class_='LeaderBoardCard_lbcWrapper__e4bCZ LeaderBoardWithButtons_lbwbCardGrid__Iqg6m LeaderBoardCard_leaderBoardCategory__vWRuZ')
rank = check.find_all('td', class_="LeaderBoardPlayerCard_lbpcTableCell__SnM1o")
name = check.find_all('a', class_="Anchor_anchor__cSc3P LeaderBoardPlayerCard_lbpcTableLink__MDNgL")
# Iterate through the tables and select the desired one based on the text within it
Name = []
Rank = []
Points = []
counter = 0
for table in rank:
    rank = table.text
    Rank.append(rank.strip(". "))
for check in name:
    name = check.text
    if counter % 2 == 0:
        Name.append(name)
    else:
        Points.append(name)
    counter +=1

print(Rank)
print(Name)
print(Points)

data = list(zip(Rank, [date] * len(Rank), Name, Points))

filename = 'data.csv'
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Rank', 'Date', 'Name', 'Point'])  # Write the header row
    writer.writerows(data)  # Write the data rows

print(f"Data written to {filename} successfully.")

