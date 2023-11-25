import requests
import sys

if len(sys.argv) != 2:
    print("Missing command-line argument")
    sys.exit(1)

try:
    bitcoins = float(sys.argv[1])
except ValueError:
    print("Command-line argument is not a number")
    sys.exit(1)

url = "https://api.coindesk.com/v1/bpi/currentprice.json"

try:
    response = requests.get(url)
    response.raise_for_status()
except requests.RequestException:
    print("Unable to fetch Bitcoin price")
    sys.exit(1)

data = response.json()
price = data["bpi"]["USD"]["rate_float"]

cost = bitcoins * price
formatted_cost = f"{cost:,.4f}"

print(f"{bitcoins} BTC = ${formatted_cost}")
