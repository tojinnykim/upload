class Customer:
    def __init__(self,name,email,age = 18):
        self.name = name
        self.email = email
        self.age = age
        self.loyalty_points = 0 #포인트
    def earn_point(self,amount):
        self.loyalty_points += amount
        return f'{self.name}님의 현재 포인트는 {self.loyalty_points}입니다.'
    def get_profile(self):
        return f'프로필:{self.name} ({self.age}세), 이메일{self.email},\
        포인트{self.loyalty_points}'

# 인스턴스 생선
c1 = Customer('홍길동','abc@abc.com',20)
print(c1.earn_point(100))
print(c1.get_profile())

#메소드 사용 

