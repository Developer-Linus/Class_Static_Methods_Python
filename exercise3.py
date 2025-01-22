class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @classmethod
    def create_child(cls, name):
        return cls(name, 0)

person1 = Person("John", 30)
person2 = Person.create_child("Jane")

print(f"Name: {person1.name}, Age: {person1.age}")
print(f"Name: {person2.name}, Age: {person2.age}")