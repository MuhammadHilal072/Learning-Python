# OOP in Python:

# Class in OOP:

class Student:
    Name = "M.Hilal"

s1 = Student()      
print(s1)
print(s1.Name)

s2 = Student()
print(s2)
print(s2.Name)

# Constructor:

class Student:
    def __init__(self, name, marks, age):
        self.name = name
        self.marks = marks
        self.age = age
        print("Adding new students to Database..")

s1 = Student("Muhammad Hilal", 88, 22)
print(s1.name, s1.marks, s1.age)

s2 = Student("Muhammad jalal", 99, 24)
print(s2.name, s2.marks, s2.age)


# Attributes :

# Class Attributes: that are common among all the instance or objects of that class 
# Object Attributes: that are differents for all the objects of the class

# class Student:
college_name = "GPGC Mardan"         # this is a class attribute because same for all the students 
def __init__(self, name, marks, age):
    self.name = name       ## these are the objects attribute that are differents for all the students 
    self.marks = marks
    self.age = age
    print("Adding new students to Database..")

s1 = Student("Muhammad Hilal", 88, 22)
print(s1.name, s1.marks, s1.age)

print(s1.college_name)


# Methods OR Functions:

class Student:
    college_name = "GPGC Mardan"

    def __init__(self, name, marks, age):
        self.name = name
        self.marks = marks
        self.age = age

    def Wellcome(self):
        print("wellcome to our college :", self.name)

    def Get_Marks(self):
        return self.marks
    
    
s1 = Student("Muhammad Hilal", 88, 22)
s1.Wellcome()
print(s1.Get_Marks())


# Question:

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def Get_Avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print(self.name, "your avg score is :", sum/3)


s1 = Student("Hilal", [72, 83, 88])
s1.Get_Avg()


# Static Methods:

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @staticmethod
    def Hello():
        print("hello :")


s1 = Student("Muhammad Hilal", 88)        
print(s1.name, s1.marks)
s1.Hello()


# Question:

class Account:
    def __init__(self, balance, acc_no):
        self.balance = balance
        self.acc_no = acc_no

    def Debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited from your account :", self.acc_no)
        print("your total balance is:", self.Get_balance())

    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited from your account :", self.acc_no) 
        print("your total balance is:", self.Get_balance())   

    def Get_balance(self):
        return self.balance

acc1 = Account(50000, 117203)
acc1.Debit(25000)
acc1.credit(50000)


# del Keyword:

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

s1 = Student("hilal", "73")
print(s1.name, s1.marks)

del s1 


# Private Attributes:

class Account:
    def __init__(self, acc_no, acc_pass, balance):
        self.__acc_no = acc_no      ## these two are private attributes
        self.__acc_pass = acc_pass  ## /////  ////  /////  /////
        self.balance = balance


# Inheritance:

class Car:
    @staticmethod
    def Start():
        print("Car is started.......")

    @staticmethod
    def Stop():
        print("Stoping the car.......")


class ToyotaCar(Car):
   
   def __init__(self, brand):
    self.brand = brand


class Fortuner(ToyotaCar):

    def __init__(self, type):
        self.type = type


car1 = Fortuner("Diesel")
print(car1.type)
car1.Start()
car1.Stop()


# Super() Method:

class Car:

    def __init__(self, type):
        self.type = type

    @staticmethod
    def Start():
        print("Car is started.......")

    @staticmethod
    def Stop():
        print("Stoping the car.......")


class ToyotaCar(Car):
   
   def __init__(self, name, type):
       self.name = name
       super().__init__(type)


c1 = ToyotaCar("priuse", "Diesel")
print(c1.type)
c1.Start()
c1.Stop()


# ClassMethod: Decorator

class Person():
    name = "hilal"
 
    # def ChageName(self, name):
    #     self.name = name
        # 1st way to change name variable value
        # Person.name = name
        # 2nd way 
        # self.__class__.name = "Muhammad Hilal"
        # 3rd way is
    @classmethod
    def ChageName(cls, name):
        cls.name = name


p1 = Person()
p1.ChageName("Muhammad Hilal")
print(p1.name)
print(Person.name)


# PropertyMethod: Decorator

class student():

    def __init__(self, phy, chem, bio):
        self.phy = phy
        self.chem = chem
        self.bio = bio

    @property
    def Percentage(self):
        return (self.phy + self.chem + self.bio) / 3 

s1 = student(98, 97, 99)
s1.chem = 90
print(s1.Percentage)

# getter and setter decorators also we can exploe it 


# Polymorphism:

# 1st thing is Operator Overloading:

print(1 + 71) # = 3
print("M" + "." + "Hilal") # means concatination
print([1, 2, 3] + [4, 5, 6]) # merege to lists

# This is called Polymorphism 


# Dunder Functions:

class Complex:
    
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def ShowNumber(self):
        print(self.real, "i +", self.img, "j")

    def __add__(self, c2):
        newreal = self.real + c2.real
        newimg = self.img + c2.img
        return Complex(newreal, newimg)
    
    def __sub__(self, c2):
        newreal = self.real - c2.real
        newimg = self.img - c2.img
        return Complex(newreal, newimg)

c1 = Complex(6, 32)
c1.ShowNumber()

c2 = Complex(4, 30)
c2.ShowNumber()

c3 = c1 + c2
c3.ShowNumber()

c4 = c1 - c2
c4.ShowNumber()


# Questions:

# Q1:

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def Area(self):
        return 3.14 * self.radius ** 2
    
    def primeter(self):
        return 2 * 3.14 * self.radius 



cir1 = Circle(21)
print(cir1.Area())
print(cir1.primeter())


# Q2:

class Employee:

    def __init__(self, role, dep, salary):
        self.role = role
        self.dep = dep
        self.salary = salary

    def ShowDetails(self):
        print("your role is :", self.role)
        print("your department is :", self.dep)
        print("your salary is :", self.salary)

class Engineer(Employee):

    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Enginerr", "electric", "75000")


e1 = Employee("lecturer", "CSE", "1,50,000")
e1.ShowDetails()

Eng1 = Engineer("Hazrat Bilal", 28)
Eng1.ShowDetails()


# Q3:

class Order:

    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, O2):
        return self.price > O2.price


O1 = Order("tea", "50")
O2 = Order("beryani", "200")

print(O1 < O2)





        


