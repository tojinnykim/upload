# 현실적으로 가장 많이 사용되는 패턴
# 매개변수가 많을 때 
# 첫번째나 두번째 혹은 만흔 3번째까지는 ㅔㅐ냐샤ㅐㅜ미
# 나머지는 전부 default parameter
# def welcome_customer(name, addr, age ): #디폴트 갑 순서대로 출력
    # return f'{name}, {age}세, {addr}지역 고객님 환영합니다' 

# print("aaaa")

# 학생들의 정보는 리스트로 받고 옵션을 줘서 다양하게 값을 리턴

def students_info(scores, is_max=None, is_min=None, is_avg=None):
    if max:
        return max(scores)
    elif min:
        return min(scores)
    elif avg:
        return sum(scores) / len(scores)
    else:
        return scores

import random
student_scores = []
for i in range(10):
    student_scores.append(random.randint(80,100))

print(f'scores = {students_info(student_scores)}')
print(f'scores = {students_info(student_scores, is_max=True)}')
