import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# ✅ Binance Futures Testnet Base URL
BASE_URL = "https://testnet.binance.vision"

# ✅ API credentials (must match keys from testnet)
API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

# ✅ Sanity check (optional)
if not API_KEY or not API_SECRET:
    raise ValueError("❌ API Key or Secret not found in environment variables.")
