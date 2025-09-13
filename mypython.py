#print("NAMASTHE,WELCOME TO MY PYTHON LEARNINGS")

#variables
""""
name="venukumkar"
print(name)
print(f"Hiii {name}")

age=21
print(f"your age is:{age}")
"""

#typecasting
'''
a=30
print(type(a))

b=30.1
print(type(b))

c=True
print(type(c))
'''

#input
'''
a=input("enter the num1: ")
b=input( "enter the num2: ")

print("number2:",a)
print("number1:",b)
'''


#string slicing
'''
a="venukumar"
shortname=a[0:4]
print(shortname)

#nagtive slicing

b="venukumar"
name=b[-9:-4]
print(name)

#slicing with skip value

c="0123456789"
print(c[0:9:3])
'''


#string functions
'''
name="prasanna dandetikar"

print(len(name))
print(name.endswith("a"))
print(name.endswith("A"))
print(name.startswith("p"))
print(name.startswith("P"))
print(name.capitalize())

replacedstring=name.replace("dandetikar","raju")
print(replacedstring)

#escape seq characters
print("venu is studying engineering\nin avanthi college")
'''

#LISTS
'''
items=["srinu",99,True,20.5]
print(items[3])

items[0]="venu"
print(items[0])
#LIST METHODS

l1=[1,2,34,5,6,67,7]
print(l1)

l1.sort()
print(l1)

l1.reverse()
print(l1)

l1.append(30)
print(l1)

l1.insert(6,99)
print(l1)

l1.pop(5)
print(l1)

l1.remove(7)
print(l1)
'''

#TUPLES
'''
a=(1,2,3,4,1,6,1,8,9)
print(type(a))

#TUPLE METHODS

b =(a.count(1))
print(b)

c=(a.index(2))
print(c)
'''


#dictionaries
'''
students={
    "name":"venu",    
    "name1":"varun",  
    "name2":"vinay"
}
print(type(students))
print(students["name2"])

students.items()
print(students)

print(students.keys())

print(students.values())

print(students.get("name1"))

print(students.copy())

print(students.pop("name"))
'''

#if else
'''
age= int(input("enter your age="))

if age >=18 and age<=100:
    print("you are eligible to vote")
elif age>100:
    print("enter right age")
elif age<0:
    print("age must be positive")        
else:
    print("not eligible to vote")    
    '''

#formatted strings
'''
fn='Venu'
ln="Dandetikar"

msg=f'{fn} [{ln}] is a student'
print(msg)
'''

#math
'''
import math

print(math.floor(2.9))
print(math.ceil(2.9))
print(math.fabs(2.9))
print(math.pow(5,2))
print(math.sqrt(4))
print(math.factorial(5))
'''

#logical operators
'''
name=True
isstudent=True

if name and isstudent:
    print("eligible to access the webpage")
if name or isstudent:
    print("check yours details again")
if name and not isstudent:
    print("eligible")
'''

#height converter game
'''
height=int(input("enter youre height(in CMs): "))
choice=input("(ft)feets or (inc)inches: ")

if choice=="ft":
    result=height//30.48
    print(f'you are {result} feet')
else:
    res=height//2.54
    print(f'you are {res} inches')    
''' 

#while
'''
i=1
while i<10:
    print(i)
    i+=1  
print("DONE")      
   
i=1
while i<10:
    print('0' * i)
    i+=1  
print("DONE")      
'''      

#number guessing game
'''
num=5
guesscount=0
guesslimit=3

while guesscount<guesslimit:
    guess=int(input("guess the num:"))
    guesscount+=1
    if guess==num:
        print("you won the game")
        break
else:
    print("you lost the game")    
'''

#for loop
'''
for item in "venumadhav":
    print(item)
for item in [1,2,3,4,5,5,6,6,6]:
    print(item)   
for item in [10]:
    print(item)      
for i in range(2,10):
    print(i)
for i in range(2,10,2):
    print(i)    
costs=[5,5,5,5,5]
j=0
for i in costs:
    j+=i
print(j) 
'''

#nested loops
'''
for i in range(1,3):
    for j in range(1,2):
        print(f'[{i},{j}]')

age=21
name="venu"
if age>18:
    if name.startswith("v"):
        print("you are admin")
    else:
        print("u r not admin")    
else:
    print("uneligible age")    

num=[1,2,3,4,5,6,7,8,9,10]      
for i in num:
    print('*'*i)  
'''    

#functions
'''
def greet_user():
    print("good morning!")
    print('have a nice day')

print('start')
greet_user()
print('end')

#parameters

def greet_user(name):
    print(f"good morning {name}!")
    print('have a nice day')

print('start')
greet_user('venu')
print('end')
'''

#return
'''
def cube(num):
    return num*num*num

res=cube(2)
print(res)
print(cube(3))
'''

#EXCEPTION
'''
try:
    a=int(input("enter a number:"))
    b=int(input("enter a number:"))
    res=a/b
    print(res)

except ZeroDivisionError:
    print("cannot divisible by 0")
'''

#classes
'''
class  Cse:
    def csea(self):
        print("this is cseA")
    def cseb(self):
        print("this is cseB")

avih  = Cse()
avih.csea()
avih.cseb()          
'''

 #OOP in python
'''
class Student:
    def __init__(self,rno,name,course):
        self.rno=rno
        self.name=name
        self.course=course
student1=Student(530,'venukumar','CSE')

print(student1.rno)
print(student1.name)
print(student1.course)
'''

#CLASS
'''
class Student:

    city="hyderabad"
    total=0

    def __init__(self,rno,name,course):
        self.rno=rno
        self.name=name
        self.course=course
        Student.total += 1
student1=Student(530,'venukumar','CSE')
student2=Student(530,'venu','CSE')
student3=Student(530,'kumar','CSE')


print(student1.rno)
print(student1.name)
print(student1.course)
print(student1.city)
print(Student.city)
print(Student.total)
'''

 #HERITANCE
'''
class Animal:
    def __init__(self,name,born):
        self.name=name
        self.born= born
        
    def eat(self):
        print("{self.name} is eating")    

class lion(Animal):
    pass

l1=lion('raju',1999)

print(l1.name)
print(l1.born)
'''


#MULTIPLE(1CHILD MORE PARENTS) and MULTILEVEL(GP,P,C) inheritance
'''
class Animal:
    def eat(self):
        print("this is eating")
    
class wild(Animal):
    def carnivore(self):
        print('this is wild animal')

class reptiles(Animal):
    def wateranimal(self):
        print('this is reptile')


class lion(wild):
    pass
class crocodile(wild,reptiles):
    pass


l1=lion()
c1=crocodile()

c1.wateranimal()
l1.carnivore()

l1.eat()
c1.eat()
'''

#SUPER()
'''
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("Dog barks")
d = Dog()
d.speak()
'''

#POLYMORPHISM
'''
from abc import ABC,abstractmethod

class shape:
    @abstractmethod 
    def area():
        pass

class circle(shape):
    def __init__(self,rad):
        self.rad=rad
    def area(self):
        return 3.14* self.rad**2  
     
class square(shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        return self.side**2

shapes=[circle(1),square(1)]

for shape in shapes:
    print(shape.area())
    print(f'{shape.area()}Sq.CM')
'''

#DUCK TYPING
'''
class Animal:
    alive=True
class dog(Animal):
    def speak(self):
        print('bow bow')

class cat(Animal):
    def speak(self):
        print('meow!')
class car(Animal):
    alive=False
    def speak(self):
        print('durrrr!')        

animals=[dog(),cat(),car()]

for animal in animals:
    animal.speak()
    print(animal.speak)
    print(animal.alive)
'''

#STATIC METHOD(NO OBJ CREATION,USED FOR SMALL CALCUL,CALL WITH CLASSNAME DIRECTLY)
'''
class MathTools:
    @staticmethod
    def add(a, b):
        return a + b
    @staticmethod
    def square(n):
        return n * n
print( MathTools.add(5, 7))      
print(MathTools.square(4))
'''

#MULTITHREADING
'''
import threading
import time

def walkdog():
    time.sleep(5)
    print('dog is walking')

def mail():    
    time.sleep(3)
    print('you got the mail')

walkdog()
mail()    
'''