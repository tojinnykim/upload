# 기본 매개변수
def welcome_customer(name, addr='서울', age = 18): #디폴트 갑 순서대로 출력
    return f'{name}, {age}세, {addr}지역 고객님 환영합니다' 

print(welcome_customer('홍길동'))
print(welcome_customer('홍길동','부산',20))
print(welcome_customer('홍길동', 20, '부산')) #이름, 지역, 나이 순으로 대입

print(welcome_customer(age = 20,addr = '경기', name = '홍길동'))
print(welcome_customer('홍길동', age = 20,))