import pandy as pd
from bs4 import BeautifulSoup
import requests
import os
data = []

rows =[]
url = 'https://learn.microsoft.com/en-us/exchange/new-features/build-numbers-and-release-dates?view=exchserver-2019'
result = requests.get(url).content
soup = BeautifulSoup(result, "html.parser")

table_body = soup.find('tbody')
rows = table_body.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele]) # Get rid of empty values
print(data)
# cells = rows.find_all('td')[0]

# for row in rows:
#     print(row)


# row_data = []
# for row in table_body.find_all('tr'):
#     col = row.find_all('td')
#     col = [ele.text.strip() for ele in col]
#     row_data.append(col)
# print(row_data)

