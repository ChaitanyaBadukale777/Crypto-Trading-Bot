import time
import hmac
import hashlib
import requests

API_KEY = "your_api_key"  # Replace with your actual API key
API_SECRET = "your_secret_key"  # Replace with your actual secret key

BASE_URL = "https://testnet.binancefuture.com"
endpoint = "/fapi/v2/balance"

timestamp = int(time.time() * 1000)
query_string = f"timestamp={timestamp}"

signature = hmac.new(API_SECRET.encode(), query_string.encode(), hashlib.sha256).hexdigest()
url = f"{BASE_URL}{endpoint}?{query_string}&signature={signature}"

headers = {
    "X-MBX-APIKEY": API_KEY
}

response = requests.get(url, headers=headers)

print("Status:", response.status_code)
print("Response:", response.text)
