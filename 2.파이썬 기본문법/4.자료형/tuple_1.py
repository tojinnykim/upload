# tuple, list, set
# tuple : 순서가 있고, 중복을 허용한다. (인덱싱 가능), 수정이 불가능 (immutable)
tuple_1 = (1,2,3,4,5,1,2,3,4)
tuple_2 = (10,20)
print("tuple_1 + tuple_2 = ", tuple_1 + tuple_2)
print("tuple_1 * 2 = ", tuple_1 * 2)
print("tuple_1[0] = ", tuple_1[0])
print("tuple_1[1:4] = ", tuple_1[1:4]) #마지막에서 -1 해야함 #슬라이싱
print("튜플의 개수는 = ", len(tuple_1))
print("tuple_1[8] = ", tuple_1[8])
print("마지막 튜플의 값 = ", tuple_1[ len(tuple_1)-1] )
print("마지막 튜플의 값 = ", tuple_1[-1] )
# 튜플의 데이터중에서 마지막 3개를 출력
print("마지막 데이터 중에서 마지막 3개의 값 = ",  tuple_1[-3: ] )
# 튜플의 데이터 중에서 처음 3개를 출력
# 역방향으로 출력
print("역 방향으로 출력을 하면=", tuple_1[::-1])
print("처음 3개의 값 = ", tuple_1[ :3] )
# 튜플의 데이터 중에서 2번째부터 6번째까지 출력