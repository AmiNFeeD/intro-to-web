#1 Simple and objects
from abc import ABC, abstractmethod

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def displayInfo(self):
        return f'{self.brand} {self.model} {self.year}'


car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Honda", "Civic", 2019)

print(car1.displayInfo())
print(car2.displayInfo())

#2 Second example

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("Alice", 25)
print(person1.name)
print(person1.age)

#3 Methods in class
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def bark(self):
        return f'{self.name} says Woof!'
dog1 = Dog("Buddy", "Golden Retriever")
print(dog1.bark())

#4 Modifying Objects Attributes

class Phone:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
phone1 = Phone("Samsung", 500)
print(phone1.price)

phone1.price = 450
print(phone1.price)

# Class vs Instance Variables

class Employee:
    def __init__(self, name,salary):
        self.name = name
        self.salary = salary
employee1 = Employee("Alice", 50000)
employee2 = Employee("Bob", 60000)

print(employee1.salary)
print(employee2.salary)

# The role of Self
class Calculator:
    def __init__(self, value):
        self.value = value
    def add(self, num):
        self.value += num
    def get_value(self):
        return self.value
calc = Calculator(10)
calc.add(5)
print(calc.get_value())

# Deleting Objects Attributes or Objects

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
user1 = User("john_doe", "john@example.com")
print(user1.email)

del user1.email
del user1

# User Authentication System

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    def login(self, password):
        if password == self.password:
            return f"Welcome, {self.username}!"
        else:
            return "Invalid credentials!"
user = User("admin", "secure123")

print(user.login("secure123"))
print(user.login("wrongpass"))

#Advanced OOP Concepts

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print (f"Deposited {amount}.New balance: {self.__balance}")
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print (f"Withdrawn {amount}.Remaining balance: {self.__balance}")
        else:
            print ("Insufficient funds")

    def get_balance(self):
        return self.__balance

account = BankAccount("Alice", 1000)
account.deposit(500)
account.withdraw(300)

print(account.get_balance())

#Inheritance
class Animal:
    def __init__(self, name):
        self.name = name
    def make_sound(self):
        return "Some sound"
class Dog(Animal):
    def make_sound(self):
        return "Woof"
class Cat(Animal):
    def make_sound(self):
        return "Meow"
dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.name, "says:", dog.make_sound())
print(cat.name, "says:", cat.make_sound())

#Polymorphism

class Bird:
    def fly(self):
        return "Flying high"
class Airplane:
    def fly(self):
        return "Taking off into the sky"
class Fish:
    def fly(self):
        return "I can not fly"

for obj in [Airplane(), Fish(), Bird()]:
    print(obj.fly())

#Abstraction
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")
class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started")
car = Car()
bike = Bike()

car.start_engine()
bike.start_engine()

#Advanced OOP Features
class Parent:
    def show(self):
        print("This is parent class")
class Child(Parent):
    def show(self):
        print("This is child class")
obj = Child()
obj.show()

class A:
    def method_a(self):
        print("Method A")
class B:
    def method_b(self):
        print("Method B")
class C(A,B):
    pass

obj = C
obj.method_a()
obj.method_b()

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def displayInfo(self):
        return f'{self.title} by {self.author} {self.year}'

class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        self.books.append(book)
    def list_books(self):
        for book in self.books:
            print(book.displayInfo())
book1 = Book("1984", "George Orwell", 1949)
book2 = Book("To Kill a MockingBird", "Harper Lee", 1960)

library = Library()
library.add_book(book1)
library.add_book(book2)
library.list_books()