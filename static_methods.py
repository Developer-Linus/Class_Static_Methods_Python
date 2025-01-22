class MathUtils:
    @staticmethod
    def add(x,y):
        return x + y

    @staticmethod
    def multiply(x,y):
        return x * y
print(MathUtils.add(5,3))
print(MathUtils.multiply(5,3))
'''
Let's break down the provided code:

Class Definition:

Defines a class named MathUtils.
Includes two static methods add and multiply.
Static methods are defined using the @staticmethod decorator.
Static methods do not require an instance of the class to be created.
Static methods can be called without creating an instance of the class.
Calling Static Methods:

Calls the add method using MathUtils.add(5, 3), which adds 5 and 3 and returns the result.
Calls the multiply method using MathUtils.multiply(5, 3), which multiplies 5 and 3 and returns the result.
Output:

8
15


This code defines a class MathUtils with two static methods:add and multiply. Static Methods:

add(a, b) method takes two arguments a and b and returns their sum.
multiply(a, b) method takes two arguments a and b and returns their product
MathUtils.add(5, 3) calls the static method add with arguments 5 and 3, returning the sum 8.
MathUtils.multiply(5, 3) calls the static method multiply with arguments 5 and 3, returning the product 15.
In the provided code, MathUtils acts as a utility class for basic arithmetic operations, demonstrating the use of static methods for encapsulating related functionality within a class without the need for instance variables or methods.
'''