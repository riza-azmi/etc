#!/usr/bin/env python
import requests
response            = requests.get("https://gist.githubusercontent.com/Jekiwijaya/c72c2de532203965bf818e5a4e5e43e3/raw/2631344d08b044a4b833caeab8a42486b87cc19a/gistfile1.txt")
historical_price    = str(response.text).split(" ")

hours_max = historical_price.index(max(historical_price))
hours_min = historical_price.index(min(historical_price[:hours_max]))

print("Buy at hour", hours_min, "\tPrice:", historical_price[hours_min])  
print("Sell at hour", hours_max, "\tPrice:", historical_price[hours_max])
print("Profit\t", int(historical_price[hours_max])-int(historical_price[hours_min]), "for", int(hours_max)-int(hours_min),"hours") 