class Student:
    def __init__(self,name,age,scores):
        self.name = name
        self.age = age
        self.scores = scores
    def __str__(self):
        return f'이름 : {self.name}, 나이 : {self.age}, 점수 : {self.scores}'
    def get_total(self):
        return sum(self.scores)
    def get_avg(self):
        return self.get_total()/len(self.scores)
    
s = Student('홍길동',20,(95,98,55))

s1 = Student('홍길동',20,(95,98,55))
s2 = Student('이순신',50,(65,48,65))

Student[
    Student('홍길동',20,(95,98,55)),
    Student('이순신',50,(65,48,65))
    ]

print(Student[0].name)
Student[0].name = '강감찬'