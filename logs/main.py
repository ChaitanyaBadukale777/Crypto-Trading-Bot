from config import API_KEY, API_SECRET
from utils import setup_logger
from bot import BasicBot

def main():
    logger = setup_logger()
    bot = BasicBot(API_KEY, API_SECRET, logger)

    print("Welcome to the Binance Testnet Trading Bot")
    print("Available Commands: market, limit, balance, exit")

    while True:
        cmd = input("\nEnter Command: ").strip().lower()

        if cmd == "market":
            symbol = input("Enter Symbol (e.g. BTCUSDT): ").upper()
            side = input("Enter Side (BUY/SELL): ").upper()
            quantity = float(input("Enter Quantity: "))
            result = bot.place_market_order(symbol, side, quantity)
            print(result)

        elif cmd == "limit":
            symbol = input("Enter Symbol (e.g. BTCUSDT): ").upper()
            side = input("Enter Side (BUY/SELL): ").upper()
            quantity = float(input("Enter Quantity: "))
            price = float(input("Enter Limit Price: "))
            result = bot.place_limit_order(symbol, side, quantity, price)
            print(result)

        elif cmd == "balance":
            asset = input("Enter Asset (default USDT): ").upper() or "USDT"
            balance = bot.get_balance(asset)
            print(balance)

        elif cmd == "exit":
            print("Exiting Trading Bot.")
            break

        else:
            print("Unknown command. Try again.")

if __name__ == "__main__":
    main()
