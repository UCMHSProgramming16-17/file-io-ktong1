# Import needed modules
import csv
import math
import requests

# Question: Compare the production of 4 different energy sources (renewable, nuclear, natrual gas, crude oil) in kJs, by month, over the last 20 years

# Define global EIA API key variable
EIA_APIkey = "a0758428314605c2172e496804668b98"
 
# Collect renewable data
def collectdata_renewable():
    
    # Define api basics
    # Note: url, with various ids and series, found on eia site
    url_renewable = "http://api.eia.gov/series/?api_key=YOUR_API_KEY_HERE&series_id=TOTAL.REPRBUS.M"
    
    # Insert EIA API key into url
    url_renewable = url_renewable.replace("YOUR_API_KEY_HERE", EIA_APIkey)
    
    # Send data requests and store in a variable
    json_renewable = requests.get(url_renewable)
    
    # Convert from json into python
    renewable_data = json_renewable.json()
    
    # Return data
    return renewable_data

# Collect nuclear data
def collectdata_nuclear():
    
    # Define api basics
    # Note: url, with various ids and series, found on eia site.
    url_nuclear = "http://api.eia.gov/series/?api_key=YOUR_API_KEY_HERE&series_id=TOTAL.NUETPUS.M"
   
    # Insert EIA API key into url
    url_nuclear = url_nuclear.replace("YOUR_API_KEY_HERE", EIA_APIkey)
    
    # Send data requests and store in a variable
    json_nuclear = requests.get(url_nuclear)
    
    # Convert from json into python
    nuclear_data = json_nuclear.json()
    
    # Return data
    return nuclear_data

# Collect natural gas data
def collectdata_naturalgas():
    
    # Define api basics
    # Note: url, with various ids and series, found on eia site
    url_naturalgas = "http://api.eia.gov/series/?api_key=YOUR_API_KEY_HERE&series_id=TOTAL.NGELPUS.M"
    
    # Insert EIA API key into url
    url_naturalgas = url_naturalgas.replace("YOUR_API_KEY_HERE", EIA_APIkey)
    
    # Send data requests and store in a variable
    json_naturalgas = requests.get(url_naturalgas)
    
    # Convert from json into python
    naturalgas_data = json_naturalgas.json()
    
    # Return data
    return naturalgas_data

# Collect oil data
def collectdata_oil():
    
    # Define api basics
    # Note: url, with various ids and series, found on eia site
    url_oil = "http://api.eia.gov/series/?api_key=YOUR_API_KEY_HERE&series_id=TOTAL.PAPRPUS.M"
    
    # Insert EIA API key into url
    url_oil = url_oil.replace("YOUR_API_KEY_HERE", EIA_APIkey)
    
    # Send data requests and store in a variable
    json_oil = requests.get(url_oil)
    
    # Convert from json into python
    oil_data = json_oil.json()
    
    # Return data
    return oil_data


# Store data in csv files  
def storedata(data, csvtitle):
    
    # Make csv files
    csvfile = open(csvtitle, "w")
    
    # Create csvwriter
    csvwriter = csv.writer(csvfile, delimiter = ",")
    
    # Put data into csv files
    
