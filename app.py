import streamlit as st
from config import API_KEY, API_SECRET
from utils import setup_logger
from bot import BasicBot

# Initialize
logger = setup_logger()
bot = BasicBot(API_KEY, API_SECRET, logger)

st.title("📈 Binance Futures Testnet Trading Bot")
st.markdown("Use this interface to place **market**, **limit**, and **stop-limit** orders on Binance Testnet.")

st.sidebar.header("🔧 Order Settings")
symbol = st.sidebar.text_input("Trading Symbol (e.g., BTCUSDT)", "BTCUSDT").upper()
side = st.sidebar.selectbox("Order Side", ["BUY", "SELL"])
quantity = st.sidebar.number_input("Quantity", min_value=0.001, value=0.01, step=0.001)

order_type = st.sidebar.radio("Order Type", ["Market", "Limit", "Stop-Limit"])

if order_type == "Limit":
    limit_price = st.sidebar.number_input("Limit Price", min_value=0.001, step=0.001)

if order_type == "Stop-Limit":
    stop_price = st.sidebar.number_input("Stop Price", min_value=0.001, step=0.001)
    limit_price = st.sidebar.number_input("Limit Price", min_value=0.001, step=0.001)

st.sidebar.markdown("---")
submit = st.sidebar.button("🚀 Place Order")

if submit:
    if order_type == "Market":
        result = bot.place_market_order(symbol, side, quantity)
        st.success("Market Order Placed!")
        st.json(result)

    elif order_type == "Limit":
        result = bot.place_limit_order(symbol, side, quantity, limit_price)
        st.success("Limit Order Placed!")
        st.json(result)

    elif order_type == "Stop-Limit":
        result = bot.place_stop_limit_order(symbol, side, quantity, stop_price, limit_price)
        st.success("Stop-Limit Order Placed!")
        st.json(result)

# Balance Section
st.markdown("## 💰 Account Balance")
if st.button("🔄 Get USDT Balance"):
    balance = bot.get_balance("USDT")
    st.write(balance)
