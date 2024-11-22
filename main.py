import requests
import json 
import os
import time 
# import access_neo4j as neo4j
# neo4j.verify_connection()
print("hay")
def clear():
       os.system('cls') if os.name == 'nt' else os.system('clear')
token_endpoint = 'https://icdaccessmanagement.who.int/connect/token'


client_id = '2369713b-a065-46ed-b75d-66d4e0036f63_86fa9505-8625-4483-91bf-daa538f0af32'

client_secret = 'vTulKBpN1gwKsC0D5Edo1917zLBqJ1HwzOx/xJXZ0ko='

scope = 'icdapi_access'

grant_type = 'client_credentials'

import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# set data to post
payload = {'client_id': client_id, 
           'client_secret': client_secret, 
           'scope': scope, 
           'grant_type': grant_type}

# make request

r = requests.post(token_endpoint, data=payload, verify=False).json()
token = r['access_token']


# access ICD API

first_entity = 'http://id.who.int/icd/entity/455013390'

# HTTP header fields to set
headers = {'Authorization':  'Bearer '+token, 
           'Accept': 'application/json', 
           'Accept-Language': 'en',
           'API-Version': 'v2'}         
# make request           



# Load data from files
with open('already_present_relationships.txt', 'r') as f:
    data= [x.strip() for x in f.readlines()]
f.close()
# build a function that take a relationship with untitled url and retuns the relationship updated with the title 
def get_titled_relationship(untitled_relationship):
           url=untitled_relationship[untitled_relationship.index("http"):]
           url_details=requests.get(url, headers=headers, verify=False).json()
           title=url_details['title']['@value']
           updated_relationship=untitled_relationship.replace(url, title)
           return updated_relationship

# loop over the data and get any relationship with untitled url
c=0
for i in range(len(data)):
           if 'http' in data[i]:
                      data[i]=get_titled_relationship(data[i])
                      clear()
                      c+=1
                      print(f'Done {i} ({c})')
                      with open('already_present_relationships.txt', 'w') as f:
                                 for i in data:
                                            f.write(i+'\n')
f.close()
with open('already_present_relationships.txt', 'r') as f:
           up_d=[x.strip() for x in f.readlines()]
           c=0
           for i in up_d:
                      if 'http' in i:
                                 print('false')
                      else:
                                 c+=1
                                 print(f'Edited {c}')
f.close()