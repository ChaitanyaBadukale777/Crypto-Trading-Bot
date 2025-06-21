# 📊 Crypto Trading Bot (Binance Futures Testnet)

A simplified automated trading bot that connects to the Binance USDT-M Futures **Testnet** using the official `python-binance` library. This bot supports Market, Limit, and Stop-Limit orders and includes full logging, error handling, and a CLI/Streamlit-ready architecture.

---

## 🚀 Features

- ✅ Place **Market**, **Limit**, and **Stop-Limit** orders
- ✅ Supports both **Buy** and **Sell** operations
- ✅ Fetch **USDT Wallet Balance**
- ✅ Works on Binance **Futures Testnet**
- ✅ Built with Python using `python-binance`
- ✅ Full logging with `bot.log` for traceability
- ✅ Modular code with `BasicBot` class
- ⚙️ Easily extendable to Streamlit / CLI

---

## 📁 Project Structure

Crypto-Trading-Bot/
├── bot.py # Main trading logic (BasicBot class)
├── config.py # Loads Binance API credentials and base URL
├── test_bot.py # Simple script to test connectivity and orders
├── logger.py # Logger utility writing logs to bot.log
├── .env # Your API credentials (not tracked in Git)
├── bot.log # Auto-generated log file
└── README.md # Project documentation



---

## 🔐 Setup API Credentials

1. Visit [Binance Futures Testnet](https://testnet.binancefuture.com).
2. Generate API Key & Secret (Note: this may redirect to Binance Vision testnet).
3. Create a `.env` file:


---

## 💻 Installation

```bash
git clone https://github.com/yourusername/Crypto-Trading-Bot.git
cd Crypto-Trading-Bot

# Install required packages
pip install -r requirements.txt
```

## Test the Bot
To test connectivity and balance:
```
python test_bot.py
```

Sample Output :
```
✅ Connected to Binance Futures Testnet.
USDT: Wallet = 15000.00000000
```
---

## ⚠️ Notes
This project uses Binance Testnet only – no real funds involved.

Ensure you’ve enabled Futures in your testnet account.

Disable IP restrictions for development use.

Check precision requirements for symbols like BTCUSDT.


## 🧑‍💻 Author
Chaitanya Badukale
GitHub: @ChaitanyaBadukale777
