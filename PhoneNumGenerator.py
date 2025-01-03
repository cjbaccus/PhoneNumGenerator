#!/usr/bin/python

#############################################################################
# Title: PhoneNumGenerator.py
#
# Authoer: Carl Baccus
#
# License: GNU GENERAL PUBLIC LICENSE
# (https://github.com/cjbaccus/PhoneNumGenerator/blob/master/LICENSE)
#
# Description and usage:
# This script is intended to be ran on cli.
# The purpose is to generate a file named "<CITY>-Num.txt"
# that has every phone number
# available in that particular City based
# on a web query lookup, and sequencing through all
# 10,000 numbers within an area-code and
# prefix for that particular city.
# This should be used for checking if numbers were not used for passwords.
# Usage: python PhoneNumGenerator.py
# # What State? <answer>
# # What City? <answer>
# result will write out file with <City>-Num.txt name.
#
#############################################################################

import re

import requests
from bs4 import BeautifulSoup

# Get user input for state and city
state = input("What state?")
City = input("What City?")

# name new file
f = open(City + "-Nums.txt", "w")
print(f)

# THis is the website to scrape data from
lookup = "https://www.area-codes.com/city/city.asp?state=" + state + "&city=" + City
print(lookup)

r = requests.get(lookup)
data = r.text
soup = BeautifulSoup(data, "lxml")

# Loops to complete number counts based on area code and prefix starters.
for link in soup.find_all('a'):
    full = link.get_text()
    num = re.sub(r'\D', "", full)
    if not (num == ""):
        if (len(num) == 6):
            for count in range(1, 9999):
                Lz = format(count, '04d')
                f.write(num + Lz + "\n")
                count = + 1
        else:
            pass
    else:
        pass

f.close()
