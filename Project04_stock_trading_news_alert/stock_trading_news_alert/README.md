# 📈 Stock Price News Alert

This Python project monitors the stock price of a selected company (e.g., Tesla) using the Alpha Vantage API. When the stock price changes significantly (default: >5%), it fetches related news using NewsAPI and sends alerts via Twilio SMS.

---

## 🚀 Features

- Tracks daily stock price fluctuations
- Calculates percentage change between consecutive days
- Fetches top 3 news articles when price volatility is detected
- Sends formatted alerts directly to your phone using Twilio

---

## 📦 Dependencies

- `requests`
- `twilio`
- `python-dotenv` 

