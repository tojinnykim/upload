import random 

print(random.sample(range(100),5)) 
print(random.randint(1,100))

list_1 = []
for _ in range(10): 
    num = random.randint(1,20)
    list_1.append(num)

print(f'list_1 = {list_1}')
