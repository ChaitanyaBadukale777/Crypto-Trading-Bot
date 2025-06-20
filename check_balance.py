from binance.client import Client
from dotenv import load_dotenv
import os

# Load .env credentials
load_dotenv()
api_key = os.getenv("BINANCE_API_KEY")
api_secret = os.getenv("BINANCE_API_SECRET")

# Initialize Futures client
client = Client(api_key, api_secret)
client.FUTURES_URL = "https://testnet.binancefuture.com"

# Fetch Futures balance
try:
    balance = client.futures_account_balance()
    print("Your Futures Testnet Balance:\n")
    for asset in balance:
        print(f"{asset['asset']}: {asset['balance']} USDT")
except Exception as e:
    print(f"Error: {e}")
