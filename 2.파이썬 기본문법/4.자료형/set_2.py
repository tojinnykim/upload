# 리스트 연산자
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
print('list_1 + list_2 = ', list_1 + list_2) #리스트 연결

list_2.extend(list_2)
print('list_1 = ',list_1) 
print('list_2 * 3 = ', list_2 * 3)
print('list_1 * 3 = ', list_1 * 3) # 리스트 반복

# 문자열 
str_1 = 'hello'
str_2 = 'world'
print('str_1 + str_2 = ', str_1 + str_2)
print('str_1 * 3 = ', str_1 * 3) # 문자열 반복
print('str_1[0] = ', str_1[0])

# set 
# 중복 허용 불가 
set_1 = {1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8}
print('set_1 = ', set_1)

# set에서 특정 위치에 단일 값에 접근하려면
# set은 집합 연산이 가능
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 5, 6, 7, 8}

#교집합
print('set_1 & set_2= ', set_1 & set_2)
print('set_1.intersection(set_2)= ', set_1.intersection(set_2)) # 위와 동일

#합집합
print('set_1 | set_2= ', set_1 | set_2)
print('set_1.union(set_2)=' , set_1.union(set_2)) # 위와 동일')

#차집합
print('set_1 -  set_2= ', set_1 - set_2)
print('set_1.diffference(set_2)=', set_1.difference(set_2))


