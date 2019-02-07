#!/usr/bin/python
def add(x, y):
   return x + y

def subtract(x, y):
   return x - y

def multiply(x, y):
   return x * y

def divide(x, y):
   return x / y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

select = int(input("Enter choice(1/2/3/4):"))

number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))

if select == 1:
	print(add(number_1, number_2))

elif select == 2:
	print(subtract(number_1, number_2))

elif select == 3:
	print(multiply(number_1, number_2))

elif select == 4:	
	print(divide(number_1, number_2))

else:
	print("invalid")

