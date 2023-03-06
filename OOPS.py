# Q--> difference between class book() and class book ??

class book():
    def __init__(self,name) -> None:
        self.__name = name
# private members of class can be represented __attribute and last written  of class will be executed. 
class book:
    def __init__(self,name):
        self.name = name

b = book("HC Varma")
# print(b.__name) --> raises an error that the attribute not exist in class and the solution for this is next step  
# print(b._book__name)

# Attribute Methods ..
# print(getattr(b,"name"))
# print(hasattr(b,"name"))
setattr(b,"age",22) #creates attribute if not exists and sets value ,id exists sets the given Value
# print(getattr(b,"age"))
delattr(b,"name")
# print(getattr(b,"name")) #raises an error as not is doesnot exists.


# *** Static methods and Class methods ***
class Newspaper:
    def __init__(self,name) -> None:
        self.name = name
    @staticmethod
    def news1(name):
        return name +" is best newspaper"
    # @classmethod --> 
    # Q--> this method raises an AttributeError: type object 'Newspaper' has no attribute 'name'..
    def news2(cls): # --> "cls" used to represent the cls method
        return cls.name + " is best newspaper"

# n = Newspaper("eenadu")
# print(n.news1("Sakshi"))
# print(n.news2())

# # Checking Instances of classes..
# print(type(n))
# print(type(b))
# print(type(n)==type(b)) # --> Hence n and b are instances of two seperate classes and thus they two are not same 
# print(isinstance(n,Newspaper))
# print(isinstance(n,object)) # --> everything in python is a subclass of object class ,so it returns True

# static and class methods,instance methods
class student:
    count = 0 #  variables
    marks = 550 # class variables
    def __init__(self,name,marks): # self ,alias instance methods 
        self.name = name # instance variables
        self.marks = marks # instance variables

    @classmethod # @classmethod taking parameters 
    def percent(cls,marks):
        return (marks/600)*100
    @classmethod # @classmethod can access 
    def newPercent(cls): # @classmethod can access class variables like cls.marks
        return (cls.marks/600)*100
    @staticmethod # @staticmethod takes parameters from class instance object or class object (line 68,69)
    def myprct(prct):
        return "my percentage is "+str(prct) 

# s1 = student("lokesh",98)
# s2 = student("yamini",100)
# print(s1.percent(500))
# print(s1.newPercent())   
# print(s1.myprct(s1.percent(500)))
# print(student.myprct(student.percent(599)))

# Magic Methods
class Book:
    def __init__(self,title,price) -> None:
        self.title = title
        self.price = price
    def __eq__(self,value): #Equal comparison of two objects
        if not isinstance(value,Book):
            raise ValueError("can't compare two different classes")
        return self.title == value.title and self.price == value.price
    def __ge__(self,value): #GreaterThan or equal to operator of two objects
        if not isinstance(value,Book):
            raise ValueError("can't compare two different objects")
        return self.price >= value.price
    def __lt__(self,value): #lessThan operator of two objects
        if not isinstance(value,Book):
            raise ValueError("can't compare two different objects")
        return self.price < value.price

B1 = Book("parrites",100)
B2 = Book("population",200)
B3 = Book("parrites",100)
# print(B1==B2 ,B1==B3)
# print(B1>=B3, B1<B2)
# Books = [B1,B2,B3]
# Books.sort() #sort() uses __lt__ i.e. lessthan operator
# for book in Books:
#     print(book.title,end = " ")


#Data Classes
from dataclasses import dataclass
@dataclass
class Book:
    title : str
    author : str
    pages : int
    price : float
    
    def __post_init__(self):
        self.description = f"{self.title} is written by {self.author} consitis of {self.pages} and price is {self.price}"
    def bookInfo(self):
        self.info = f"{self.title}, {self.author} pages{self.pages} and price is {self.price}"

b1 = Book("war and peace","jack",89,40.0)
b2 = Book("Marvel","joe",90,89.0)

print(b1) # works like __repr__
print(b1.title)
print(b1==b2)
print(b1.description) #Because of __post_init__
print(b1.bookInfo())
