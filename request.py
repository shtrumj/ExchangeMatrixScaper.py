from bs4 import BeautifulSoup
import requests
#
BASE = "http://127.0.0.1:5000/"
#
response = requests.get(BASE + "exchangecu")
#
# print(response.json())
import re
import requests

# BASE = "https://mail.trot.co.il/owa"

# response = requests.get(BASE)
# soup = BeautifulSoup(response.content, 'html.parser')

# res= soup(response.text)

# Exchange2019 = (re.search("15.02.\d\d\d\d.\d\d\d",str(soup)).group())
print(response.text)