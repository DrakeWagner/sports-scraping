import requests
import csv
from bs4 import BeautifulSoup
import datetime

URL = 'https://www.foxsports.com/mlb/standings'
result = requests.get(URL)

print(result.status_code) #200
src = result.content
soup = BeautifulSoup(src, 'html.parser')
print(soup.title)

links=[]
for i in links:
    links.append(i.get('href'))


table=soup.find('table')
for i in table.select('tr'):
    col = i.select('th')
    if col:
        division = col[0].text.strip()
        print(division)

tables=soup.findAll('table')
for i in tables.selectAll('tr'):
    col = i.select('th')
    if col:
        division = col[0].text.strip()
        print(division)
    

# filename formatting
today = datetime.datetime.now()
today = today.strftime('%m-%d-%y')
datetime.datetime.now().date().isoformat()

# write to csv