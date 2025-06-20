from binance.client import Client
from config import API_KEY, API_SECRET  # imports from your config.py

# Correct Futures Testnet base URL
client = Client(API_KEY, API_SECRET)
client.FUTURES_URL = "https://testnet.binancefuture.com"

try:
    # Try fetching Futures account info
    acc_info = client.futures_account()
    print("✅ Connected to Binance Futures Testnet")
    print("Available Assets:\n")
    for asset in acc_info['assets']:
        print(f"{asset['asset']}: Wallet Balance = {asset['walletBalance']}")
except Exception as e:
    print("❌ Error:", e)