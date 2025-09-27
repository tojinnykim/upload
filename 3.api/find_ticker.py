import yfinance as yf

# 한국 주요 종목 코드 매핑
STOCKS = {
    '삼성전자': '005930.KS', 'SK하이닉스': '000660.KS', 'NAVER': '035420.KS', '네이버': '035420.KS',
    '카카오': '035720.KS', 'LG화학': '051910.KS', '현대차': '005380.KS', '기아': '000270.KS',
    'POSCO홀딩스': '005490.KS', '포스코홀딩스': '005490.KS', 'LG에너지솔루션': '373220.KS',
    '삼성바이오로직스': '207940.KS', '셀트리온': '068270.KS', 'KB금융': '105560.KS',
    '신한지주': '055550.KS', 'LG전자': '066570.KS', '현대모비스': '012330.KS',
    'SK텔레콤': '017670.KS', 'KT&G': '033780.KS', '한국전력': '015760.KS'
}

def find_stock(name):
    """종목명으로 코드 찾기 (정확 매칭 + 부분 매칭)"""
    # 정확 매칭
    if name in STOCKS:
        return [(name, STOCKS[name])]
    
    # 부분 매칭
    matches = [(stock_name, code) for stock_name, code in STOCKS.items() 
               if name in stock_name or stock_name in name]
    return matches

def get_stock_data(ticker):
    """주식 데이터 가져오기"""
    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(period="2d")
        
        if hist.empty:
            return None
            
        current = hist['Close'].iloc[-1]
        prev = hist['Close'].iloc[-2] if len(hist) >= 2 else current
        change = current - prev
        change_pct = (change / prev) * 100
        
        return {
            'price': current,
            'change': change,
            'change_pct': change_pct,
            'volume': hist['Volume'].iloc[-1]
        }
    except:
        return None

def main():
    print("한국 주식 조회 (종료: quit)")
    print(f"지원 종목: {', '.join(sorted(STOCKS.keys()))}")
    
    while True:
        name = input("\n종목명 입력: ").strip()
        
        if name.lower() in ['quit', 'q', '종료']:
            break
            
        matches = find_stock(name)
        
        if not matches:
            print(f"'{name}' 종목을 찾을 수 없습니다.")
            continue
            
        if len(matches) > 1:
            print("검색 결과:")
            for i, (stock_name, _) in enumerate(matches, 1):
                print(f"{i}. {stock_name}")
            continue
            
        stock_name, ticker = matches[0]
        data = get_stock_data(ticker)
        
        if not data:
            print("데이터를 가져올 수 없습니다.")
            continue
            
        # 결과 출력
        sign = "▲" if data['change'] > 0 else "▼" if data['change'] < 0 else "-"
        print(f"\n{stock_name} ({ticker})")
        print(f"현재가: {data['price']:,.0f}원")
        print(f"전일대비: {data['change']:+,.0f}원 ({data['change_pct']:+.2f}%) {sign}")
        print(f"거래량: {data['volume']:,.0f}")

if __name__ == "__main__":
    main()