import requests
import requests_oauthlib
from requests_oauthlib import OAuth2Session
import oauthlib.oauth2
from oauthlib.oauth2 import BackendApplicationClient
import json


path = 'C:\\users\\public\\keys.txt'
f = open(path, "r")
keys = f.read().split('\n')

#redirect_uri = 'https://github.com/Dhagemann7/ShelterWalletScraper'

client = BackendApplicationClient(client_id=keys[0])
oauth = OAuth2Session(client=client)
token = oauth.fetch_token(token_url='https://api.petfinder.com/v2/oauth2/token', client_id=keys[0],
        client_secret=keys[1])
oauthToken = token['access_token']
header = {'Authorization': 'Bearer '+oauthToken}

#29 chosen because there are currently 565 pages at 20 per page.  565/20 ~ 28
#Find current count at https://www.petfinder.com/animal-shelters-and-rescues/search/
#Pages start at 1.
organizationLinks = []
for x in range(1,29):
    r = requests.get(url = 'https://api.petfinder.com/v2/organizations?limit=100&page='+str(x), headers = header)
    jsonBlock = (json.loads(r.text))
    organizationList = jsonBlock['organizations']
    for x in range(len(organizationList)): 
        if((organizationList[x]['website']) != None): organizationLinks.append(organizationList[x]['website'])
print(organizationLinks)
