nums = [1, 2, 3, 4, 5, 6]
print(f"numbers = {nums}")



even_list = []
for num in nums:
    if num % 2 == 0:
        even_list.append(num)
print(f"짝수의 값 = {even_list}")



name = "Alice"
scores = [80, 90, 100]
average = sum(scores) / len(scores) 

print(f"Student: {name}, Scores: {scores}, Average: {average}")



students = [
    {"name":"jinny", "scores":[80,90,95]},
    {"name":"tom", "scores":[20,45,80]}
    ]
for student in students:
    average = sum(student["scores"]) / len(student["scores"])
    print(f"Student : {student['name']}, Scores: {student['scores']}, Average: {average}")



students = [
    {"name":"jinny", "scores":[80,90,95]},
    {"name":"tom", "scores":[20,45,80]},
    {"name":"jason", "scores":[35,65,90]}
    ]
for student in students:
    average = sum(student["scores"]) / len(student["scores"])
    print(f"Student : {student['name']}, Average: {average:.1f}")

students = [
    {"name":"jinny", "scores":[80,90,95]},
    {"name":"tom", "scores":[20,45,90]},
    {"name":"jason", "scores":[35,65,90]}
    ]
best_students = None
best_average = 0

for student in students:
    average = sum(student["scores"]) / len(student["scores"])
    highest = max(student["scores"])

    print(f"Studnets: {student['name']}, Average: {average:.1f}, Highest Score: {highest}")

    if average > best_average:
        best_average = average
        best_students = student["name"]
        

print(f"\nBest Students: {best_students} with average {best_average}")