#!/usr/bin/python

#make list of all valid phone numbers for a city.
# this is a work in progress.
# 
import pandas as pd
import requests
import re
from bs4 import BeautifulSoup
from tabulate import tabulate

#Main function
#areaCodes = ["669205", "669327", "408413", "408422", "408427", "408430", "408442", "669500", "408632", "408665", "408713", "408767", "408840", "408842", "408843", "408846", "408847", "408848", "408852"]

# for ac in areaCodes:
#     for num in range(1, 9999):
#         lz = format(num, '04d')
#         print(ac + lz)
#         num = num + 1
#         

state = "CA"
City = "Gilroy"
lookup = "https://www.area-codes.com/city/city.asp?state="+ state + "&city=" + City
print(lookup)

r = requests.get(lookup)

data = r.text
soup = BeautifulSoup(data, "lxml")
#table = soup.find_all('td')[70]

#t2 = table.find_all('a')[:4]
for link in soup.find_all('a'):
    full = link.get_text()
    num = re.sub(r'\D', "", full)
    print(num)
