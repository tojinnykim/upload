#함수를 매개변술로 받는 함수
def calc(func,a,b):
    return func(a,b)

def plus(a,b):
    return a+b

def minus(a,b):
    return a-b

print(calc(plus,10,20))
print(calc(minus,10,20))
print(list(calc(range,1,10)))

import random
print(calc(random.randint,1,10))

# 람다함수는 이름없이 기능만 제공하는 함수 재사용 불가
# 함술를 매개변수로 사용하는 함수에 제공하는 역할
# lambda x : x*2

def tem(x):
    return x*2
print(tem(10))

# def multi(a,b)
#     return a*b
# print(multi(10,20))

calc(lambda a,b : a*b, 10, 20)
print(calc(lambda a,b : a*b, 10, 20))