import yfinance as yf
from datetime import datetime

def get_stock_info(ticker: str):
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        return {
            "price": info["currentPrice"],
            "name":  info["longName"],
        }
    except Exception:
        return None

def get_risk_free_rate():
    irx = yf.Ticker("^IRX")        
    rate = irx.info["regularMarketPrice"]
    return rate / 100

def time_to_expiry(expiry_date: str):
    today = datetime.today()
    expiry = datetime.strptime(expiry_date, "%Y-%m-%d")
    days = (expiry - today).days
    return days / 365

def get_expiries(ticker: str):
    stock = yf.Ticker(ticker)
    return stock.options

def get_option_chain(ticker: str, expiry: str):
    stock = yf.Ticker(ticker)
    chain = stock.option_chain(expiry)
    return chain.calls, chain.puts