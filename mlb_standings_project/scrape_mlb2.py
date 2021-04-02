# gets player rankings

import requests
import csv
from bs4 import BeautifulSoup
import datetime
import re

page = requests.get('https://www.espn.com/mlb/history/leaders/_/breakdown/season/year/2020')
soup = BeautifulSoup(page.text, 'html.parser')

headers = soup.find_all('tr', attrs={'class' : 'colhead'})

body = soup.find('table', attrs={'class':'tablehead'})
# for i in body:
#     players = soup.find_all('tr', attrs={'class':re.compile('row player-10-')})#, attrs={'class':'oddrow player-10-33039'})
#     for i in players.find_all('td'):
#         print(i.get_text())
    
stats=[]
names=[]
# players = soup.find_all('tr', attrs={'class':re.compile('row player-10-')})
# for i in players:
#     stats_list=([y.get_text() for y in i.find_all('td')])
#     names.append((stats_list[1]))


# gets list of names on page
name_cell = soup.findAll(attrs={'class':re.compile('player-10-')})
for i in name_cell:
    name = i.find('span', attrs={'class':'bi'})
    if name is not None:
        names.append(name.text) 

# get all stats from row
row = soup.find_all('tr', attrs={'class':re.compile('player-10-')})
for i in row:
    for stat in i.find_all('td'):
        stats.append(stat.get_text())

# alternate names
# test case
print(names)
print(stats[1::16]) # use revised names
for i in stats[1::16]:
    if i not in names:
        print(i)

# assign colnames
cols: ['', 'PLAYER', 'YRS', 'G', 'AB', 'R', 'H', '2B', '3B', 'HR', 'RBI', 'BB', 'SO', 'SB', 'CS', 'BA']

RANK = stats[0::16]
PLAYER = stats[1::16]
YRS = stats[2::16]
G = stats[3::16]
AB = stats[4::16]
R = stats[5::16]
H = stats[6::16]
DOUBLES = stats[7::16]
TRIPLES = stats[8::16]
HR = stats[9::16]
RBI = stats[10::16]
BB = stats[11::16]
SO = stats[12::16]
SB = stats[13::16]
CS = stats[14::16]
BA = stats[15::16]


# iterate through to create into csv formatting
def Extract(lst, num):
    return [item[num] for item in lst]

rows=[]
data =  [RANK, PLAYER, YRS, G, AB, R, H, DOUBLES, TRIPLES, HR, RBI, BB, SO, SB, CS, BA]
length = len(RANK)
for i in data:
    for num in range(length):
        rows.append(Extract(data, num))



# take column names from table
cols = []
header = soup.find('tr', attrs={'class':'colhead'})
for i in header.find_all('td'):
    cols.append(i.get_text())


# filename formatting
today = datetime.datetime.now()
today = today.strftime('%m-%d-%y')
datetime.datetime.now().date().isoformat()

# write to csv
with open('player_stats_{}'.format(today), 'w') as f:
    write = csv.writer(f)
    write.writerow(cols)
    write.writerows(rows)
    

'''

As of April 2

'''
# my_dict = dict()
# # iterate through and collect stats
# def stats_list(col_num, variable_name):
#     mylist = []
#     for i in stats[col_num::16]: #16 different columns
#         mylist.append(i)
#     my_dict[variable_name] = mylist

# # send lists to select column names
# # loop through colnames and add list to each?

# # cols: ['', 'PLAYER', 'YRS', 'G', 'AB', 'R', 'H', '2B', '3B', 'HR', 'RBI', 'BB', 'SO', 'SB', 'CS', 'BA']

# # for i in cols:
# #     my_dict[i] = stats_list(cols.index(i)) # each group of stats printed in order

# print(my_dict)

# # iterate through and add keys to values
# keys = ('', 'PLAYER', 'YRS', 'G', 'AB', 'R', 'H', '2B', '3B', 'HR', 'RBI', 'BB', 'SO', 'SB', 'CS', 'BA')
# for i in range(0, 16):
#     stats_list(i, keys[i])
