import time
import hmac
import hashlib
import requests

API_KEY = "Mt0nPd3ejn2HajrN3fxM3BMDgswJMvVZ0nN7p21gzvG3Vx0MBkIGL4Z2SBTfVjcv"
API_SECRET = "cRmXZHe6UIODqCkN6vTcoMQ6P30W2Ssirh0oDrqZS2LGYQeoVoFDxtWMagqJMhCU"

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
