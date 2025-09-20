# 고객 별 구매 금액을 딕셔너리로 맵핑
# 구매 금액을 조회 
# 없는 고객을ㄹ 조회하려고 하면 에러 발생 
# try ~ except ~ else 사용해서 키가 없는 경우 처리, 정상적인 경우엔 추가작업

#구매고객 리스트 
customer_purchase = {'김민수' :15000, '홍길동' :230000, '박소연':45000}

while True:
    # 고객 이름을 받아서 조회
    search_name = input('검색하려는 고객 이름을 입력하세요: ') #존재하지 않는 고객
    try:
        amount = customer_purchase[search_name]
    except KeyError:
        print(f'오류: {search_name} 고객 데이터가 없습니다')
    else:
        print(f'{search_name} 고객의 구매 금액은: {amount}원')
        break
