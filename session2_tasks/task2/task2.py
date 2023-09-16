"""**************************************************************************************************************************************************
Description:   This code is to get BTC last updated price

**************************************************************************************************************************************************"""
import requests
request = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
BTC = request.json() #mandatory to convert raw data into json, dictionary
#print("Wait here")
print(f"BTC price= {BTC['bpi']['USD']['rate']}\nLast upadate: {BTC['time']['updated']}") #Note, parsing dict using '' not ""