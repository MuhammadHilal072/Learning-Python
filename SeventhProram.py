# File I/O in Python:

# Deleting a File:

import os
os.remove("demo.txt")


# Reading a File:

f = open("demo.txt", "r")
data = f.read()
print(data)
print(type(data))


line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)

f.close()

# Writing to a File:

f = open("demo.txt", "w")
f.write("I am going university tomorrow.               ")
f.close()

f = open("demo.txt", "a")
f.write("\n I will Take a class. \n and then back to home")
f.close()


with open("demo.txt", "r") as f:
    data = f.read()

    print(data)

with open("demo.txt", "w") as f:
    f.write("okay thanks see you tomorrow")



# Questions:

# Q1:

with open("practice.txt", "w") as p:
    p.write("Hi everyone\nwe are learning File I/O\nusing Java.\nI like programming in Java.")

# Q2:

def Read_Write():
    with open("practice.txt", "r") as p:
        data = p.read()
        print(data)
        new_data = data.replace("Java", "Python")
        print(new_data)
        with open("practice.txt", "w") as p:
            p.write(new_data)

Read_Write()

# Q3:

def Check_Word():
    with open("practice.txt", "r") as p:
        data = p.read()
        print(data)    
        if(data.find("learning") != -1):
            print("FOUND")
        else:
            print("NOT FOUND")

Check_Word()

        
# Q4:

def Check_Line():
    data = True
    line_no = 1
    with open("practice.txt", "r") as p:
        while(data):
            data = p.readline()
            if(data.find("programming") != -1):
                print(line_no)
                return
            line_no += 1

    return -1


Check_Line()



