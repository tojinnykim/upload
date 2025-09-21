# 함수 전달하는 매개변수가 가변적일때ㅐ
# temp(1)
# temp(1,2)
# temp(1,2,3,4,3,2,3,4,3)

# 가변 매개변수
def temp(*params): #패킹 packing ""*""를 빼면 갯수가 안맞는 에러가 발생
    print(type(params))
    for i in params:
        pass #적절한 로직
        print(i)

temp(1,2,3,4,5)

def temp(params): #패킹 packing ""*""를 빼면 갯수가 안맞는 에러가 발생
    print(type(params))
    for i in params:
        pass #적절한 로직
        print(i)

temp((1,2,3,4,5))

# def temp(params): #패킹 packing ""*""를 빼면 갯수가 안맞는 에러가 발생
#     print(type(params))
#     for i in params:
#         pass #적절한 로직
#         print(i)

# temp(1,2,3,4,5)

# b1 = (100,10)
# print(f'b1 = {b1}')

# a1, a2 = (100,10) #unpackin
# print(f'a1= : {a1}')
# print(f'a2= : {a2}')

def Test(*args,name):
    pass

# Test(1,2,3)은 Error
Test(1,2,3, name='홍길동')

# positional, default, 가변매개변수, 
def Test(*args,data): Test(1,2,3,4) #1,2,3,4가 모두 args로 가져감 에러 발생
def Test(data,*args): Test(1,2,3,4) #1을 data로 가져감. 실행됨

print()