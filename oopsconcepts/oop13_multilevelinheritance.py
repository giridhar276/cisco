
class Person:
    def details(self):
        print("I am a person")

class Employee(Person):
    def role(self):
        print("I am an employee")

class Intern(Employee):
    def stipend(self):
        print("I get a stipend")

i = Intern()
i.details()   # Person
i.role()      # Employee
i.stipend()   # Intern
