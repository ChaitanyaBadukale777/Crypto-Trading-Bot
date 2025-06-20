from binance.client import Client
from binance.exceptions import BinanceAPIException
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("BINANCE_API_KEY")
api_secret = os.getenv("BINANCE_API_SECRET")

# ✅ Instantiate client with correct URL
client = Client(api_key, api_secret)
client.FUTURES_URL = "https://testnet.binancefuture.com"

try:
    # ✅ Fetch Futures account info
    acc = client.futures_account()
    print("✅ Connected to Futures Testnet!")
    for asset in acc['assets']:
        print(f"{asset['asset']}: Wallet = {asset['walletBalance']}")

except BinanceAPIException as bapi:
    print("❌ Binance API error:", bapi)
except Exception as e:
    print("❌ Other error:", repr(e))
