# 비교연산자
# ==, !=, >, <, >=, <=
# is, is not
# is : 객체의 동일성(주소값)을 비교
# == : 객체의 동등성(값)을 비교

a = [1, 2, 3]
b = [1, 2, 3]
b = a
print(a == b)      # True (값을 비교)
print(a is b)     # False (주소값을 비교)

# in, not in
# 시퀀스 자료형(문자열, 리스트, 튜플, 딕셔너리(key값), set)에서 사용
# 특정 값이 시퀀스 자료형에 포함되어 있는지 확인
print(1 in [1, 2, 3])        # True

# 논리연산자
# and, or, not
# and : 둘 다 참일 때 참
# or : 둘 중 하나만 참이어도 참
# not : 참 -> 거짓, 거짓 -> 참
x = 0
x > 5 and x < 10 # 6,7,8,9

age = 0
age <= 8 or age >= 65 # 0~7, 66~
kor = 0 ; eng = 0 ; math = 0 ; avg = 0
avg > 60 and kor >=40 and eng >=40 and math >=40
