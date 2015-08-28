import requests
import csv

zip = "94109"

def get_estimated_rent_prices(zip):
    url = "https://www.quandl.com/api/v1/datasets/ZILL/Z{}_RAH.csv".format(zip)
    response = requests.get(url=url)
    prices = []
    for entry in response.content.split("\n"):
        prices.append(entry.split(','))
    prices_dict = {}
    for i in prices[1:len(prices)-1]:
        prices_dict[i[0]] = float(i[1])
    return prices_dict
    
if __name__ == "__main__":
    return get_estimated_rent_prices(zip)
