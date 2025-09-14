# 학생 성적 관리 프로그램

# 학생 정보를 저장할 빈 튜플 리스트 초기화
students = []

# 학생 수 입력받기
student_count = int(input("학생 수를 입력하세요: "))

# 각 학생의 이름과 성적 입력받기
for i in range(student_count):
    name = input(f"{i+1}번째 학생의 이름을 입력하세요: ")
    score = float(input(f"{name}의 성적을 입력하세요: "))
    # (이름, 성적) 형태의 튜플을 리스트에 추가
    students.append((name, score))

# 성적을 기준으로 정렬하여 석차 계산
# 성적이 높은 순으로 정렬
sorted_students = sorted(students, key=lambda x: x[1], reverse=True)

# 결과 출력
print("\n== 학생 성적 석차 ==")
print("석차\t이름\t성적")
print("-" * 20)

for rank, (name, score) in enumerate(sorted_students, 1):
    print(f"{rank}등\t{name}\t{score}")

# 검색 기능
while True:
    search_name = input("\n검색할 학생 이름을 입력하세요 (종료: q): ")
    if search_name.lower() == 'q':
        break
        
    # 학생 찾기
    found = False
    for rank, (name, score) in enumerate(sorted_students, 1):
        if name == search_name:
            print(f"\n{name}학생의 성적은 {score}점이고, {rank}등 입니다.")
            found = True
            break
    
    if not found:
        print("해당 학생을 찾을 수 없습니다.")

print("\n프로그램을 종료합니다.")
