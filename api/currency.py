import requests

binance_api_url = "https://api.binance.com/api/v3/ticker/price"


def getBtcPriceMessage():
    response = requests.get(binance_api_url, params={"symbol": "BTCUSDT"})
    data = float(response.json()["price"])
    text = f"1 BTC = {data} USDT"
    return text
