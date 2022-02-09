class Person():
    def display1(self):
        print("This is superclass")


# subclass
class Employee(Person):
    def display2(self):
        print("This is subclass")


emp = Employee()

emp.display1()
emp.display2()