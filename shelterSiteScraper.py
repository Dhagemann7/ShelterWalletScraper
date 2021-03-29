from bs4 import BeautifulSoup
import csv
import os
import lxml
import requests

dir_path = os.path.dirname(os.path.realpath(__file__))
f = open(dir_path+'\\data\\petFinderLinks.txt', "r")
links = f.read().split('\n')
f.close()
links = links[0].split(',')
for x in range(len(links)):
    links[x] = links[x].split("'")[1]

page = requests.get(links[0])
soup = BeautifulSoup(page.text,'html.parser')

print(soup.prettify())

