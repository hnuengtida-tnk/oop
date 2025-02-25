import requests

api_key = 'QP8H5KFKKZTHPGVT'
function = 'TIME_SERIES_DAILY'
symbol = 'AAPL'

url = f'https://www.alphavantage.co/query?function={function}&symbol={symbol}&apikey={api_key}'
url_json = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AAPL&apikey=QP8H5KFKKZTHPGVT'

result = requests.get(url).json()
print(result)

Information = result['name']
Symbol = result ['sys'] ['country']
LastRefreshed =result ['weather'] [0]['main'] 
TimeZone = result ['weather'] [0] ['description']



  "1. Information": "Daily Prices (open, high, low, close) and Volumes",
        "2. Symbol": "AAPL",
        "3. Last Refreshed": "2025-01-17",
        "4. Output Size": "Compact",
        "5. Time Zone": "US/Eastern"