# 매출 보고서
date = ['월', '화', '수', '목', '금']
sales = [25000,18000,30000,22000,15000]
# 총 매출과 평균 매출를 출력
# 평균 이상 매출이ㅣ 일어난 요일을 출력 

# 총 매출, 평균 매출
total_sales = sum(sales) #sum() 함수는 리스트의 모든 요소의 합을 반환
average_sales = total_sales / len(sales) #len() 함수는 리스트의 길이(요소의 개수)를 반환
print(f'총 매출: {total_sales}원, 평균 : {average_sales}')

#평균 이상 매출이 일어난 요일
for idx, sales in enumerate(sales): #enumerate() 함수는 리스트의 인덱스와 값을 동시에 반환
    if sales >= average_sales:
        print(f'평균 이상 매출이 일어난 요일: {date[idx]}')
    