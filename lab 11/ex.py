#basic list oper
numbers = [10, 20, 30, 40, 50]
numbers.append(60)
numbers.insert(1, 15)
numbers.remove(30)
numbers.reverse()
numbers.sort()
print(numbers)

#List Slicing and Indexing

print(numbers[:3]) #first 3 elem
print(numbers[-2:]) # last 2 elem
print(numbers[::-1]) # reverse order

#Dictionary
student = {"name": "Alice", "age": 22, "grade": "A"}
student["subject"] = "Math"
student.update({"grade": "A+"})
student.pop("age")

print(student.keys())
print(student.values())
print(student.items())

#sets

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
union = set1.union(set2)
intersection = set1.intersection(set2)
difference = set1.difference(set2)

print(union)
print(intersection)
print(difference)

#tuple
colors = ("red", "blue", "green", "red", "yellow")
print(colors.index("green"))
print(colors.count("red"))

#Nested

company = {"employees":[
    {"name": "Ceaser", "position": "model", "salary": "$20 000"},
    {"name": "Speedwagon", "position": "CEO", "salary": "$40 000"}]}
company["employees"].append({"name": "John", "position": "accountant", "salary": "$30 000"})
for employee in company["employees"]:
    print(employee["name"])