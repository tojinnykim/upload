import yfinance as yf

# 삼성전자 (KOSPI: 005930.KQ → Yahoo 심볼은 '005930.KQ' 또는 '005930.KS')
ticker_symbol = "005930.KS"
stock = yf.Ticker(ticker_symbol)

# 최근 5일간 주가 데이터
data = stock.history(period="5d")
print(stock.info['currentPrice'])