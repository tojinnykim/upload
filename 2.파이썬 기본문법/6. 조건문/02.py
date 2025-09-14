score = 85
if score >= 70:
    print('70점 이상입니다)')

list_1 = [1, 2, 3, 4, 5]
if 2 in list_1:
    print("2가 포함되어 있습니다.")

dict_1={'name':'홍길동', 'age':30}
if 'name' in dict_1:
    print("name이 dict_1포함되어 있습니다.")

# 중첩 조건문
# if 조건문1
#     if 조건문2:
#         실행문
#     else:
#         실행문
# 예시
num = 10
if num > 0:
    if num % 2 == 0:
        print("양수이면서 짝수입니다.")
    else:
        print("양수이면서 홀수입니다.")
else:
    print("음수입니다.")

num = 1
if num % 2 == 0:
    if num % 3 == 0:
        print("2와 3의 공배수입니다.")
    else:
        print("2의 배수입니다.")
else:
    print("음수입니다.")

if num % 2 == 0 and num % 3 == 0:
    print("2와 3의 공배수입니다.")
    
if True:
    print("항상 실행되는 문장")
    print("if와 상관없는 문장")