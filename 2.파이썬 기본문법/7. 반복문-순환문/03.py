#continue

count = 0 #초기값
while count < 10: # 조건문
  count += 1 #count 1씩 증가
  if count == 5: 
    break #5일때 반복문 탈출
  print(f'count: = {count}') #5는 출력되지 않음 #break 만나면 반복문 탈출

count = 0
while count < 10: # 조건문
  count += 1 #count 1씩 증가
  if count == 5: 
    continue #5일때는 아래 코드 실행 안하고 다시 조건문으로 올라감
  print(f'count: = {count}') #5는 출력되지 않음 #continue 만나면 아래 코드 실행 안하고 다시 조건문으로 올라감 