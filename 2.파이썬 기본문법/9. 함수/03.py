# 이름을 입력하면 주어진 야식으로 인사말ㅇ를 출력하는 함수
# def hello(name):
#     print(f"{name}님 안녕하세요")

# print( hello("홍길동") )

def validate_eamil(data):
    # .com , .co.kr , .jr
    if '@' in data and '.com' in data or '.co.kr' in data or '.jr' in data:
        return True
    else:
        return False
    
customer_email = 'abc@abc.com'
is_valid = validate_eamil(customer_email)
print(f'이메일 {customer_email} 검증 : {is_valid}')