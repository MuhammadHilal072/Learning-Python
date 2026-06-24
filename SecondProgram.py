# String in Python:

str1 = "M.Hilal in from of string" 
str2 = 'from Mardan'
str3 = """a software engineer"""
str4 = "This is second program in python. \n This is my first program in python. \t This is my second program in python. \n This is my third program in python."

print(str4)

finalstr = str1 + str2 + str3

print(finalstr)
print(len(finalstr))

str = "M.Hilal"
print(str[1:5])

str = "i am studying python programming language"

print(str.endswith("language"))
print(str.upper())
print(str.capitalize())
print(str.replace("python", "java"))
print(str.find("python"))
print(str.count("python"))


FirstName = str(input("Enter your first name :"))
print(len(FirstName))


# Conditinal Statements in Python:

Age = 16
if(Age >= 18):
    print("Yor are eligibale fro vote ")
elif(Age == 17):
    print("You are not eligibale for vote but you are 17 years old.")
else:
    print("You are not eligibale for vote because you are under 18 years old.")
  

# Question:
Marks = int(input("ENter your marks :"))
if(Marks >= 90):
    print("your grade is A")
elif(Marks >=80 and Marks < 90):
    print("your grade is B")
elif(Marks >= 70 and Marks < 80):
    print("your grade is C")
else:
    print("your grade is D")
  
  
# Quesion:
Number = int(input("Enter a number :"))
if(Number % 2 == 0):
    print("The number is even.")
else:
    print("the number is odd.")
  

# Question:
num1 = int(input("Enter first number :"))
num2 = int(input("Enter second number :"))
num3 = int(input("Enter third number :"))
num4 = int(input("Enter fourth number :"))

if(num1 > num2 and num1 > num3 and num1 > num4):
    print(num1, " is the largest number.")
elif(num2 > num3 and num2 > num4):
    print(num2, " is the largest number.")
elif(num3 > num4):
    print(num3, " is the largest number.")
else:
    print(num4, " is the largest number.")
  

# Question:
num1 = int(input("Enter first number :"))
if(num1 % 7 == 0):
    print(num1, "is multiple of 7.")
else:
    print(num1, "is not multiple of 7.")

