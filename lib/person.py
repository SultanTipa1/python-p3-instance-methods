#!/usr/bin/env python3

class Person:
    # Class body goes here
    def _init_(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    #Instance method definition
    def talk(self):
        print("Hello World!")

    def walk(self):
        print("The person is walking.")

if __name__ == "_main_":
    person = Person("John", 22, "Male")
    person.talk()

    person.walk()
