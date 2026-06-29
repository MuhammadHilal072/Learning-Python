# Functions in Python:

def Cal_Sum(num1, num2):
    sum = num1 + num2
    print(sum)
    return sum

Cal_Sum(10, 62)

def Personal_Info():
    print("Name is M.Hilal")
    print("Age is 20")
    print("From Mardan")
    print("Learning Python for Agentic AI jurney ")


Personal_Info()
Personal_Info()
Personal_Info()
Personal_Info()
Personal_Info()


def CalAverage(a, b, c):
    sum = a + b + c
    avg = sum / 3
    print(avg)
    return avg

CalAverage(1, 2, 3)


# Questions:

# Q1:

list = [2, 3, 4, 5, 6, 1, 2, 3, 4, 5,]

def CalLen(list):
    print(len(list))

CalLen(list)

# Q2:

list2 = ["M", "u", "h", "a", "m", "m", "a", "d"]

def printEle(list2):
    for ele in list2:
        print(ele, end="")
    print(list2)

printEle(list2)

# Q3:

def CalFact(n):
    fact = 1
    for num in range(1, n+1):
        fact *= num
    print(fact)

CalFact(5)

# Q4:

def Converter(usd_val):
    inr_val = usd_val * 94.53
    print(usd_val, "USD =", inr_val, "INR")

Converter(73)

# Q5:

def CheckNum(num):
    if(num % 2 == 0):
        print(num, "is EVEN")
    else:
        print(num, "is ODD")

CheckNum(72)


# Recursion in Python:

def PrintNum(n):
    if(n == 0):
        return
    print(n)
    PrintNum(n-1)

PrintNum(8)

def CalFact(num):
    if(num == 0 or num == 1):
        return 1
    else: 
        return CalFact(num-1) * num
    
print(CalFact(5))

# Questions:

# Q1:

def CalSum(n):
    if(n == 0):
        return 0
    else: 
        print(n)
        return CalSum(n-1) + n

sum = CalSum(5)
print("The sum of these numbers is :", sum)

# Q3:

list = ["H", "i", "l", "a", "l"]

def PrintEle(list, idx):
    if(idx == len(list)):
        return
    else:
        print(list[idx])
        PrintEle(list, idx + 1)

PrintEle(list, 0)


