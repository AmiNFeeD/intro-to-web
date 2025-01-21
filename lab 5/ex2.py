# Name and Age
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Hi, {name}! You are {age} years old!")

# Sum, Average, and Product
num1, num2, num3 = map(int, input("Enter three numbers separated by space").split())
total = num1 + num2 + num3
average = total / 3
product = num1 * num2 * num3
print(f"Sum: {total}, Average: {average}, Product: {product}")