class Person:
    count = 0
    def __init__(self, name):
        self.name = name
        Person.count +=1
    @classmethod
    def display_count(cls):
        print(f"Total persons created: {cls.count}")

person1 = Person("John")
person2 = Person("Jane")
Person.display_count()

'''
Let’s break down the provided code :

Class Definition:

Defines a class named Person to represent individuals.
Has a class variable count initialized to 0, which will count the number of instances created from this class.
Includes an __init__ method (constructor) that takes a name parameter to initialize the name attribute for each person object.
Increments the count class variable by 1 every time a new instance of Person is created, using Person.count += 1 within the constructor.
Class Method (display_count):

Defines a class method display_count using the @classmethod decorator.
Class methods take the class itself cls as the first parameter instead of the instance (self).
Prints the total number of persons created by accessing the count class variable.
Creating Person Instances:

Creates two instances of the Person class named person1 and person2 with names “Alice” and “Bob”, respectively.
Using the Class Method:

Calls the display_count class method using Person.display_count() to print the total number of persons created.
'''