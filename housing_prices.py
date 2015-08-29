#!/usr/bin/env python
import requests

zipcode = "94109"
code = "PRR"

# Below are the codes for all types of readable information

data_types = {
"A": "All Homes",
"SF": "Single Family Residences",
"C": "Condominiums",
"MVSF": "Price per Square Foot",
"1B": "1 Bedroom",
"2B": "2 Bedroom",
"3B": "3 Bedroom",
"4B": "4 Bedroom",
"5B": "5 Bedroom",
"BT": "Bottom Tier",
"MT": "Middle Tier",
"TT": "Top Tier",
"RMP": "Median Rent, Homes Listed for Rent",
"RAH": "Estimated Rent, All Homes in Region",
"RZSF": "Estimated Rent per Square Foot",
"PRR": "Price-to-Rent Ratio",
"MLP": "Median List Price",
"MSP": "Median Sale Price",
"MLPSF": "Median List Price per Square Foot",
"MSPSF": "Median Sale Price per Square Foot",
"LPC": "Listing with Price Cut in Lastt 30 Days",
"MPC": "Median Price Cut",
"SLPR": "Ratio of Sale Price to List Price",
"SFL": "Sold for Loss",
"SFG": "Sold for Gain",
"IV": "Increasing Values",
"DV": "Decreasing Values",
"SPY": "Turnover in Housing Market, Past 1 Year",
"HR": "Number of Homes for Rent",
"HF": "Monthly Foreclosures per 10,000 Homes",
"FR": "Percentage of Sales / Foreclosures"
             }

def get_estimated_rent_prices(zipcode, code):
    url = "https://www.quandl.com/api/v1/datasets/ZILL/Z{}_{}.csv".format(zipcode, code)
    response = requests.get(url=url)
    prices = []
    for entry in response.content.split("\n"):
        prices.append(entry.split(','))
    prices_dict = {}
    for i in prices[1:len(prices)-1]:
        prices_dict[i[0]] = float(i[1])
    aggregated_data = {"description": data_types[code], code : prices_dict}
    return aggregated_data
    
if __name__ == "__main__":
   print  get_estimated_rent_prices(zipcode, code)
