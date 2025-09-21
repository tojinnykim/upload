class Teacher:
    def __init__(self,name):
        self.name = name

# 객체 생성
print('객체 생성전')
t = Teacher('지니') # 객체를 생성할때는 반드시 내부의 생성자가 호출 __inint__(self)
print('객체 생성후')
print(t.name)
print(type(t))

t.age = 10
print(t.age)