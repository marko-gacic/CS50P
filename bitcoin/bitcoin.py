import sys
import requests

# Check if the command-line argument is provided
if len(sys.argv) < 2:
    print("Missing command-line argument")
    sys.exit(1)

# Get the number of Bitcoins from the command-line argument
try:
    bitcoins = float(sys.argv[1])
except ValueError:
    print("Command-line argument is not a number")
    sys.exit(1)

# Query the API for the Bitcoin price
try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    if response.status_code != 200:
        print("Failed to fetch the Bitcoin price from the API:", response.text)
        sys.exit(1)
    data = response.json()
    price = data["bpi"]["USD"]["rate_float"]
except (requests.RequestException, KeyError) as e:
    print("An error occurred:", str(e))
    sys.exit(1)

# Calculate the total cost in USD
total_cost = bitcoins * price

# Format and print the result
print(f"${total_cost:,.4f}")
