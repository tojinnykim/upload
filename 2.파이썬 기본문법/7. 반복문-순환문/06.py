# 두개의 집잡 - 리스트 
# 한개는 과일 이름
# 한개는 과일 가격
# 두개의 리스트는 순서대로 데이터가 저장


fruit = ['사과', '바나나', '포도', '오렌지']
price = [100, 200, 150, 400]

#과일 가격이 200원 이상인 과일을 출력
for i in price:
    if i >= 200:
        index = price.index(i)
        print(f'{fruit[index]} : {i}원') #Wrong if duplicate values exist

if len(fruit) == len(price):
    for i in range(len(fruit)):
        if price[i] >= 200:
            print(f'{fruit[i]} : {price[i]}원')

for idx, i in enumerate(price):
    if i>=200:
        print(f'200원 이상인 과일은 : {fruit[idx]}')
