# for
    # 순환하는 횟수가 지정
    #(range(), 자료구조(list, tuple, set, dict) 등)
#while
    # 횟수는 없고 매 순환할때마다 조건을 판단해서 True

#5번 반복
for i in range(5):
    print(i)

for i in list(range(5)):
    print(i)

#자료구조를 반복
for name in ["a", "b", "c"]:
    print(name)

#tuple 자료 순환
tuple_1 = (10,20,30)
for i in tuple_1:
    print(f'i = {i}')

set_1 = {1,5,10} #set은 순서를 보장하지 않아서 순환할때마다 순서가 바뀔 수 있음
for i in set_1:
    print(f'i = {i}')

#dict 자료 순환
dict_1 = {
    "name":"홍길동",
    "age":20,
    "addr":"서울시"
}
for i in dict_1:
    print(f'i = {i}') #key값이 순환, value가 아님

for i in dict_1.values():
    print(f'i = {i}') #value값이 순환, key가 아님

for i in dict_1.keys():
    print(f'i = {i}') #key값이 순환, value가 아님

for i in dict_1.items():
    print(f'i = {i}') #itmes()는 key, value 쌍으로 튜플을 만들어서 순환

print(dict_1.items())
print(list(dict_1.items()))