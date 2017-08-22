#!/usr/bin/python

#make list of all valid phone numbers for a city.
# this is a work in progress.
# 
import pandas as pd
import requests
import re
from bs4 import BeautifulSoup
      
state = raw_input("What state?")
City = raw_input("What City?")

f = open(City + "-Nums.txt", "w")

# state = "CA"
# City = "Gilroy"
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
    if not (num == ""):
        if (len(num)==6):
            for count in range(1, 9999):
                Lz = format(count, '04d')
                f.write(num + Lz + "\n")
                print(num + Lz)
                count = + 1
        else:
            pass
    else:
        pass

f.close()