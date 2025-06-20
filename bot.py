from binance.client import Client
from binance.enums import *
from binance.exceptions import BinanceAPIException

class BasicBot:
    def __init__(self, api_key, api_secret, logger):
        self.logger = logger
        self.client = Client(api_key, api_secret)

        # ✅ Override correct HTTPS base URL
        self.client.API_URL = "https://testnet.binance.vision"


    def place_market_order(self, symbol, side, quantity):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type=ORDER_TYPE_MARKET,
                quantity=quantity,
            )
            self.logger.info(f"Market Order: {order}")
            return order
        except BinanceAPIException as e:
            self.logger.error(f"Market Order Failed: {e}")
            return {"error": str(e)}

    def place_limit_order(self, symbol, side, quantity, price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type=ORDER_TYPE_LIMIT,
                timeInForce=TIME_IN_FORCE_GTC,
                quantity=quantity,
                price=price,
            )
            self.logger.info(f"Limit Order: {order}")
            return order
        except BinanceAPIException as e:
            self.logger.error(f"Limit Order Failed: {e}")
            return {"error": str(e)}

    def get_balance(self, asset="USDT"):
        try:
            balance = self.client.futures_account_balance()
            asset_balance = next(item for item in balance if item['asset'] == asset)
            return asset_balance
        except Exception as e:
            self.logger.error(f"Error fetching balance: {e}")
            return {"error": str(e)}
