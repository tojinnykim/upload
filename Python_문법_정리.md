# 파이썬 기본 문법 정리

## 1. 기본 입출력
### 출력 (print)
```python
print('hello, world')  # 문자열 출력
print(10 + 20)        # 수식 출력
print("10 + 20 =", 10 + 20)  # 문자열과 수식 함께 출력
```

### 입력 (input)
```python
name = input("이름을 입력하세요: ")  # 사용자로부터 입력 받기
age = int(input("나이를 입력하세요: "))  # 숫자 입력 받기 (문자열을 정수로 변환)
```

## 2. 변수와 자료형
### 변수 선언과 할당
```python
name = "홍길동"    # 문자열
age = 25         # 정수
height = 175.5   # 실수
is_student = True  # 불리언
```

### 기본 자료형
1. **정수형 (int)**
   - 양수, 음수, 0을 포함하는 정수

2. **실수형 (float)**
   - 소수점이 있는 숫자
   
3. **문자열 (str)**
   - 작은따옴표나 큰따옴표로 묶인 텍스트

4. **불리언 (bool)**
   - True 또는 False 값

## 3. 컬렉션 자료형

### 리스트 (List)
- 순서가 있는 데이터의 집합
- 중복 허용
- 수정 가능
```python
scores = [10, 20, 30, 40, 50]
scores.append(60)      # 마지막에 추가
scores.insert(1, 25)   # 특정 위치에 삽입
scores.pop()           # 마지막 요소 제거
del scores[0]          # 특정 위치 요소 제거
```

### 튜플 (Tuple)
- 순서가 있는 데이터의 집합
- 중복 허용
- 수정 불가능 (immutable)
```python
coordinates = (10, 20)
first = coordinates[0]   # 인덱싱
slice = coordinates[0:2] # 슬라이싱
```

### 세트 (Set)
- 순서가 없는 데이터의 집합
- 중복 불허용
- 집합 연산 가능
```python
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# 집합 연산
intersection = set1 & set2  # 교집합
union = set1 | set2        # 합집합
difference = set1 - set2   # 차집합
```

### 딕셔너리 (Dictionary)
- 키-값 쌍으로 이루어진 데이터 집합
- 키는 중복 불가, 값은 중복 가능
```python
person = {
    'name': '홍길동',
    'age': 20,
    'city': '서울'
}
person['age'] = 21     # 값 수정
person['job'] = '학생'  # 새로운 키-값 추가
```

## 4. 조건문
### if 문
```python
score = 85
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
else:
    grade = 'F'
```

### 중첩 조건문
```python
num = 10
if num > 0:
    if num % 2 == 0:
        print("양수이면서 짝수입니다.")
    else:
        print("양수이면서 홀수입니다.")
else:
    print("음수입니다.")
```

## 5. 비교 연산자와 논리 연산자
### 비교 연산자
- `==`: 같다
- `!=`: 다르다
- `>`, `<`: 크다, 작다
- `>=`, `<=`: 크거나 같다, 작거나 같다
- `is`: 객체 동일성 비교
- `in`: 포함 여부 확인

### 논리 연산자
- `and`: 모두 참일 때 참
- `or`: 하나라도 참이면 참
- `not`: 참/거짓 반전

## 6. 데이터 복사
### 얕은 복사 vs 깊은 복사
```python
# 얕은 복사 (참조 복사)
a = [10, 20]
b = a  # a와 b는 같은 객체를 참조

# 깊은 복사
a = [10, 20]
b = a.copy()  # a와 b는 다른 객체
```

## 7. 프로그래밍 예시
### 학생 성적 관리 프로그램
```python
students = []
student_count = int(input("학생 수를 입력하세요: "))

for i in range(student_count):
    name = input(f"{i+1}번째 학생의 이름을 입력하세요: ")
    score = float(input(f"{name}의 성적을 입력하세요: "))
    students.append((name, score))

# 성적순 정렬
sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
```

이상의 내용은 프로젝트에서 발견된 주요 파이썬 문법과 개념을 정리한 것입니다. 각 섹션은 실제 코드 예제와 함께 설명되어 있어 이해하기 쉽게 구성되어 있습니다.