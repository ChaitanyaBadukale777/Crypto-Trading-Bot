from binance.client import Client
from binance.enums import *
from binance.exceptions import BinanceAPIException

# Manually define STOP (not included in binance.enums)
ORDER_TYPE_STOP = "STOP"

class BasicBot:
    def __init__(self, api_key, api_secret, logger):
        self.logger = logger
        self.client = Client(api_key, api_secret)

        # ✅ Set Testnet Base URL for Futures
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    def place_market_order(self, symbol, side, quantity):
        try:
            quantity = round(quantity, 3)
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
            quantity = round(quantity, 3)
            price = round(price, 2)
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

    def place_stop_limit_order(self, symbol, side, quantity, stop_price, limit_price):
        try:
            quantity = round(quantity, 3)
            stop_price = round(stop_price, 2)
            limit_price = round(limit_price, 2)

            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type=ORDER_TYPE_STOP,
                timeInForce=TIME_IN_FORCE_GTC,
                quantity=quantity,
                stopPrice=stop_price,
                price=limit_price,
            )
            self.logger.info(f"Stop-Limit Order: {order}")
            return order
        except BinanceAPIException as e:
            self.logger.error(f"Stop-Limit Order Failed: {e}")
            return {"error": str(e)}

    def get_balance(self, asset="USDT"):
        try:
            balance = self.client.futures_account_balance()
            asset_balance = next(item for item in balance if item['asset'] == asset)
            self.logger.info(f"Balance fetched: {asset_balance}")
            return asset_balance
        except Exception as e:
            self.logger.error(f"Error fetching balance: {e}")
            return {"error": str(e)}
