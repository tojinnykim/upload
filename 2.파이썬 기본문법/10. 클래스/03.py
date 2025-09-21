class Customer:
    def __init__(self,name,email,age = 18):
        self.name = name
        self.email = email
        self.age = age
        self.loyalty_points = 0
# 인스턴스 생선
customer1 = Customer('홍길동','abc@abc.com',20)
customer2 = Customer('이순신','lee@abc.com')
#속성에 접근해서 출력

print(customer1.name, customer1.email, customer1.age)
print(customer2.name, customer2.email)
print(customer1.loyalty_points)

