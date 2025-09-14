#dictionary
# key:value
# key는 중복 불가, value는 중복 가능
# [] () {2,3} abc = {'이름':'홍길동' , 'age':20}
# abc['취미'] abc.get('취미','없음')
# abc['age'] = 30 
# abc['취미'] = "축구"

dict_1 = {} #set? #dictonary? #빈껍데기면 딕셔너리, 데이터가 들어가면 SET
print(dict_1)
# print(type(dict_1  ))
dict_1['name'] = '홍길동'
print(dict_1)
dict_1['age'] = '20'
print(dict_1)
dict_1['age'] = '200'
print(dict_1)