# import needed modules
import csv
import math
import requests

# Question: Compare the production of 4 different energy sources (renewable, nuclear, natrual gas, crude oil) in kJs, by month, over the last 20 years

# Collect necessary data and store data in a csv file
def collectdata():
    # define api basics
    # Note: url, with various ids and series, found on eia site.
    EIA_APIkey = "a0758428314605c2172e496804668b98"
    url_renewable = "http://api.eia.gov/series/?api_key=YOUR_API_KEY_HERE&series_id=TOTAL.REPRBUS.M"
    url_nuclear = "http://api.eia.gov/series/?api_key=YOUR_API_KEY_HERE&series_id=TOTAL.NUETPUS.M"
    url_naturalgas = "http://api.eia.gov/series/?api_key=YOUR_API_KEY_HERE&series_id=TOTAL.NGELPUS.M"
    url_oil = "http://api.eia.gov/series/?api_key=YOUR_API_KEY_HERE&series_id=TOTAL.PAPRPUS.M"
    
    # Insert EIA API key into url
    url_renewable = url_renewable.replace("YOUR_API_KEY_HERE", EIA_APIkey)
    url_nuclear = url_nuclear.replace("YOUR_API_KEY_HERE", EIA_APIkey)
    url_naturalgas = url_naturalgas.replace("YOUR_API_KEY_HERE", EIA_APIkey)
    url_oil = url_oil.replace("YOUR_API_KEY_HERE", EIA_APIkey)
    
    # Send data requests and store in a variable
    json_renewable = requests.get(url_renewable)
    json_nuclear = requests.get(url_nuclear)
    json_naturalgas = requests.get(url_naturalgas)
    json_oil = requests.get(url_oil)
    
    # Convert from json into python
    renewable_data = json_renewable.json()
    nuclear_data = json_nuclear.json()
    naturalgas_data = json_naturalgas.json()
    oil_data = json_oil.json()
    
    # Put data into csv files
    
    print (oil_data)

collectdata()