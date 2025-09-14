# SET의 기본 사용법
# - 중복을 허용하지 않는다. 
# - 순서가 없다.(인덱싱으로 접근 불가)
# - 집합연산 가능(교집합, 합집합, 차집합)
# - 서로 다른 자료형끼리 전환이 가능하다 (리스트, <-> 튜플)

# 1. SET 생성 및 중복 제거 특성
numbers = {1, 2, 2, 3, 3, 4, 5}  # 중복된 2와 3은 한 번만 저장됨
print("중복이 제거된 SET:", numbers)  # 출력: {1, 2, 3, 4, 5}

# 2. 순서가 없는 특성 확인
fruits = {'apple', 'banana', 'orange'}
print("SET의 요소:", fruits)  # 매번 출력 순서가 다를 수 있음
# print(fruits[0])  # TypeError: 'set' object is not subscriptable

# 3. 집합 연산
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# 교집합
print("교집합:", set1 & set2)  # 출력: {4, 5}
print("intersection:", set1.intersection(set2))  # 위와 동일

# 합집합
print("합집합:", set1 | set2)  # 출력: {1, 2, 3, 4, 5, 6, 7, 8}
print("union:", set1.union(set2))  # 위와 동일

# 차집합
print("차집합(set1-set2):", set1 - set2)  # 출력: {1, 2, 3}
print("difference:", set1.difference(set2))  # 위와 동일

# 4. 자료형 변환
# 리스트 -> SET -> 리스트 변환
my_list = [1, 2, 2, 3, 3, 3]
my_set = set(my_list)  # 리스트를 SET으로 변환 (중복 제거)
unique_list = list(my_set)  # SET을 다시 리스트로 변환
print("원본 리스트:", my_list)
print("중복 제거된 리스트:", unique_list)