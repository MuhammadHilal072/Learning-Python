# Output in Python:

print("Hello World")
print("This is my first progra in python")
print("my name is M.Hilal.", "My age is 20.", " I am  Software Engineer.")
print(20)
print(20+30)

# Variables in Python:

Name = "M.Hilal"
Age = 20
Address = "Mardan"
Age1 = Age
RollNo = 72.22
Old = False
A = None

print(Name)
print(Age)
print(Address)

print("My name is :", Name)
print("My age  is :", Age)
print("My address is :" , Address)
print(Age1)

print(type(Name))
print(type(Age))
print(type(RollNo))

print(type(Old))
print(type(A))


a = 10
b = 62
sum = a + b
print("The sum of two numbers is :",sum)


"""Multi line comments method use three double quotes"""


# 1.Arthmetic Operators:

a = 10
b = 62
sum = a + b
sum = a - b
sum = a * b
sum = a / b
sum = a % b # mean to find out the remainder of two or more numbers
sum = a ** b # mean to find out the power of two or more numbers
print("The sum of two numbers is :",sum)


# 2.Relational Operators:

a = 10
b = 62

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)


# 3.Assignment Operators:

num = 62

num = num + 10 
num += 10
num = num - 10
num -= 10
num /= 10
num *= 10
num %= 10
num **= 10
print(num)

# 4.Logical Operators:

a = 10
b = 20

print(not False)
print(not True)
a = True
b = False

print("AND operator :", a and b)
print("OR operator :", a or b)


# Input in Python:

name =input("Enter your name : ")
input1 = input("Enter your age :")
print("wellcome", name)
print("Your age is:", input1)


name = str(input("Enter your nme :"))
age = int(input("Enter your age :"))
marks = float(input(("Enter your marks :")))

print("Your name is :", name)
print("Your age is :", age)
print("Your marks are :", marks)


# Question:
val1 = int(input("enter your first number :"))
val2 = int(input("ENter your sencond number :"))

print("The fist value is:", val1)
print("The second Value is :", val2)
sum = val1 + val2
print("The sum of these values is:", sum)