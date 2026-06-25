# List in Python:

marks = [72.2, 85.5, 90.0, 78.5, 88.0]
print(marks)
print(type(marks))
print(marks[0])
print(marks[4])
print(len(marks))

info = ["Hilal", 22, "Mardan"]
print(info)
info[0] = "Muhammad Hilal"
print(info)

# List Slicing:

marks = [72.2, 85.5, 90.0, 78.5, 88.0]
print(marks[2:4])

# List Method:

marks = [72.2, 85.5, 90.0, 78.5, 88.0]

marks.append(95.0)
print(marks)
marks.sort()
print(marks)
marks.reverse()
print(marks)
marks.insert(0, 100.0)
print(marks)
marks.pop(3)
print(marks)


# Tuples in Python:

MarksTuple = (72.2, 85.5, 90.0, 78.5, 88.0)
SingleValueTuple = (72.2,)   #The last comma is neccessary to define a single value tuple

print(type(MarksTuple))
print(MarksTuple[0])



# Question:

Input1 = str(input("Enter your first Fav moive :"))
Input2 = str(input("Enter your second Fav moive :"))
Input3 = str(input("Enter your third Fav moive :"))

FavMovies = []

FavMovies.append(Input1)
FavMovies.append(Input2)
FavMovies.append(Input3)

print(FavMovies)

# Question:

list1 = [1, 2, 3, 4]

Copylist1 = list1.copy()
Copylist1.reverse()

if (list1 == Copylist1):
    print("the list is Palindrome")
else:
    print("Not Palindrome")

# Question:

gradeTuple = ("C", "D", "A", "A", "B", "B", "A")
print(gradeTuple.count("A"))


gradeList =["C", "D", "A", "A", "B", "B", "A"]
gradeList.sort()
print(gradeList)

              
              
