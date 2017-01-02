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
    
    