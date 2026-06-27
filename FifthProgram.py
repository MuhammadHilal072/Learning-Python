# Loops in Python:

# 1. While Loop:

count = 1
while count <= 10:
    print("Hello world")
    count += 1

print(count)

i = 0

while i <= 6:
    print(i)
    i += 1

print("loop ended")


i = 6

while i >= 0:
    print(i)
    i -= 1

print("loop ended")


# Question 1:

i = 1
while i <= 100:
    print(i)
    i += 1

print("numbers upto hundered")

# Question 2:

i = 100
while i >= 1:
    print(i)
    i -= 1

print("numbers from hundered to one ..")

# Question 3:

i = 1
n = int(input("Enter your number :"))
while i <= 10:
    print(n * i)
    i += 1

print("this is the ", n ," multiplication table ")


# Question 4:

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81,100] 
idx = 0
while idx < len(nums):
    print(nums[idx])
    idx += 1 

print("this is :")


# Question 5:

nums = (1, 4, 9, 16, 25, 36, 49, 64, 81,100)
x = int(input("Enter your number :"))
i = 0

while i < len(nums):
    if(x == nums[i]):
        print("found it the index ", i)
    i += 1


nums = (1, 4, 9, 16, 25, 36, 49, 64, 81,100)
x = int(input("Enter your number :"))
i = 0

while i < len(nums):
    if(x == nums[i]):
        print("found it the index ", i)
        break
    else:
        print("finding....")
    i += 1

# 2. For Loop:

list = [1, 2, 3, 4, 5, 6, 5, 4, 3]

mix = ["potato", "tomato", "orange", "banana", "apple"]
for val in mix:
    print(val)


str = "Muhammad Hilal"

for char in str:
    print(char)
else:
    print("The End")



# Question 1:

list = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

for val in list:
    print(val)
else:
    print("End")


# Question 2:

tuple = (1, 4, 9, 16, 25, 36, 49, 64, 81,100)

x = int(input("Enter your number to search :"))
idx = 0
i = 0

for val in tuple:
    if(x == val):
        print("Element is found ", idx)
        break
    idx += 1
else:
    print("not found")


# Range method/function with fro loop:

for val in range(10):
    print(val)

for val in range(0, 72):
    print(val)

for val in range(0, 72, 2):
    print(val)


# Q1:

for val in range(1, 101):
    print(val)


# Q2:

for val in range(100, 0, -1):
    print(val)

# Q3:

x = int(input("Enter your number :"))

for val in range(1, 11):
    print(x * val)

# Pass Keyword:

for i in range(7):
    pass

print("this is an empty for loop")


# Questions:


# Q1:

n = 10
sum = 0
i = 1
while i <= n:
    print(i)
    sum += i
    i += 1

print("the sum is :", sum)

n = 10
sum = 0

for val in range(1, n+1):
    print(val)
    sum += val

print("the sum is :", sum)   


# Q2:

n = 5
fact = 1
i = 1

while i <= n:
    print(i)
    fact *= i
    i += 1

print("the factorail is :", fact)


n = 6
fact = 1

for val in range(1, n+1):
    print(val)
    fact *= val

print("the factorail is = ", fact)


