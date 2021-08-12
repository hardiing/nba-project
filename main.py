from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

year = 2021  # year to be scraped

url = "https://www.basketball-reference.com/leagues/NBA_2021_per_game.html".format(year)  # webpage containing data

html = urlopen(url)  # open the webpage

soup = BeautifulSoup(html, features="html.parser")  # convert web page into an object

soup.findAll('tr', limit=2)  # findAll to get column headers within <tr> tag

headers = [th.getText() for th in soup.findAll('tr', limit=2)[0].findAll('th')]  # getText pulls text we need for headers into list
headers = headers[1:]  # exclude first column header (rankings)

rows = soup.findAll('tr')[1:]  # findAll to get row values, excluding header row

player_stats = [[td.getText() for td in rows[i].findAll('td')] for i in range(len(rows))]  # getText pulls text we need for stats into list

stats = pd.DataFrame(player_stats, columns=headers)  # create data frame with data in headers/player_stats lists
print(stats.head(10))  # print first ten results
stats.to_csv('stats.csv')  # export data to csv


