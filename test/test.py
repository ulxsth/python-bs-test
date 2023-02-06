import requests
from bs4 import BeautifulSoup

url = ""
res = requests.get()
soup = BeautifulSoup(res.text, "html.parser")