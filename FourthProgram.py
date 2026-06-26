# Dictionary in Python:

PersonalInfo = {
    "Name" : "M.Hilal",
    "Age" : 20,
    "Address" : "Mardan",
    "Learning" : "Python"
}

print(PersonalInfo)
print(PersonalInfo["Address"])
print(PersonalInfo["Learning"])

PersonalInfo["Name"] = "Hilal"
print(PersonalInfo)
PersonalInfo["FirstName"] = "Muhammad"
print(PersonalInfo)


# Nested Dictionary:

PersonalInfo = {
    "Name" : "M.Hilal",
    "Age" : 20,
    "Address" : "Mardan",
    "Learning" : "Python",
    "Eduacation" : {
        "Matric" : 922,
        "FSc" : 900,
        "4SemesterGpa" : 3.32
    }
}

print(PersonalInfo)
print(PersonalInfo["Eduacation"])
print(PersonalInfo["Eduacation"]["FSc"])


# Dictionary Methods:

PersonalInfo = {
    "Name" : "M.Hilal",
    "Age" : 20,
    "Address" : "Mardan",
    "Learning" : "Python",
    "Eduacation" : {
        "Matric" : 922,
        "FSc" : 900,
        "4SemesterGpa" : 3.32
    }
}

print(PersonalInfo.keys())
print(tuple(PersonalInfo.values()))
print(list(PersonalInfo.values()))
print(PersonalInfo.items())
print(PersonalInfo.get("Address"))

PersonalInfo.update({"FatherName" : "Zareen Taj"})
print(PersonalInfo)


# Sets in Python:

collection = {1, 2, 3, 3, 4, 4, "M", "hilal"}
print(collection)

collect = () #   that is an empty Set 


# Set Methods:

collect = {1, 2, 3, 3, 4, 4, "M", "hilal"}
collect1 = {1, 2, 3, 5, 6, 7, 8, 9, 10}

collect.add(5)
collect.remove("M")
collect.clear()
print(collect.pop())
print(collect)
print(collect.union(collect1))
print(collect.intersection(collect1))


# Question:

PythonDict = {
    "Table" : ["a piece of furniture", "list of facts & figures "],
    "cat" : "a small animal"
}

print(PythonDict)

# Question:

subjects = {"python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"}

print(subjects)
print(len(subjects))

# Question:

SubjectDict = {}

Input1 = int(input("Enter subject1 marks:"))
Input2 = int(input("Enter subject2 marks:"))
Input3 = int(input("Enter subject3 marks:"))

SubjectDict.update({"Math" : Input1})
SubjectDict.update({"Phy" : Input2})
SubjectDict.update({"Bio" : Input3})

print(SubjectDict)

# Question:

value = {9, "9.0"}
value = {
    ("float", 9),
    ("int", 9.0)
}

print(value)

