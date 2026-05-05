import requests
import pandas as pd
import os

# create folder
os.makedirs("data", exist_ok=True)

url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd"

try:
    response = requests.get(url)
    response.raise_for_status()  # check API error
    
    data = response.json()
    
    df = pd.DataFrame(data)
    df.to_csv("data/raw_data.csv", index=False)

    print("Data extracted successfully!")

except Exception as e:
    print("Error during extraction:", e)