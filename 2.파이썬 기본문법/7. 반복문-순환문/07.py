# 고객 리스트 출력
list_1 = ['김', '이', '박', '최', '홍']
list_2 = ['철수', '영희', '민수', '지우', '길동']
import random
print(random.choice(list_1)) #list_1에서 랜덤으로 하나 출력
customers = []
for i in range(10):
    name = random.choice(list_1) + random.choice(list_2)
    customers.append(name)


# 고객 리스트 출력
for idx, i in enumerate(customers):
    print(f'고객: {i}')

for i in customers :
    print(f'고객: {i}') #더 간단한 방법

print('-'*100)
# 고객 별 구매 금액 10000~200000원 사이의 랜덤한 금액
purchases = []
for _ in range(10):
    purchases.append(random.randint(10,50)*10000)

# 총 구매금액
total_price = 0
for i in purchases:
    total_price += i
#total_price = sum(purchase) #더 간단한 방법
print(f'총 구매금액: {total_price}원')

# 25000원 이상 구매한 고객의 수
customer_counts = 0
for i in purchases:
    if i >= 25000:
        customer_counts += 1  
print(f'25000원 이상 구매한 고객 수: {customer_counts}명')  

# 25000원 이상 구매한 고객의 이름
customer_count = 0
for i in purchases:
    if i >= 25000:
        customer_count += 1
        print(f'25000원 이상 구매한 고객 명단: {customers[idx]}, {i}원')     

for idx, price in enumerate(purchases):
    if price >= 25000:
        print(f'고객명: {customers[idx]}, 구매가격: {price}원')  #더 간단한 방법

