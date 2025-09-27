# 리스트에 데이터 추가하는 법
# 맨 마지막에 추가
# 중간에 추가

# 리스트변수
scores = [10,20,30]

#append() → 하나 추가 (맨 뒤)
scores.append (100)
print(scores)

data = 10   # 처음엔 10 저장
data = 30   # 이제 data는 30으로 덮어쓰기 → 10 사라짐
data = 20   # 다시 20으로 덮어쓰기 → 30도 사라짐
print(data) # 최종 20만 남음

# Insert() → 원하는 위치에 삽입, append(x) → 항상 맨 뒤에 추가
scores.insert(1,200)
print(scores)

# delete → 위치로 삭제 (돌려주진 않음)
del scores[0]
print(scores)

# pop → 위치로 삭제 (꺼낸 값도 돌려줌), 인덱스를 안 넣으면 → 마지막 값 삭제
scores.pop(0)
print(scores)

# remove(값) → 리스트에서 처음 발견된 값 하나만 삭제
# 중복 값이 있으면, remove()를 여러 번 호출해야 다 지워짐
# 만약 리스트에 그 값이 더 이상 없는데 remove() 하면 ValueError 발생
# insert(i, x) → i번째 위치에 끼워 넣음 (기존 값들은 한 칸씩 뒤로 밀림)