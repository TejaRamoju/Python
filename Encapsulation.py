class Employee:
    def __init__(self, name, salary, project):
        self.name = name
        self.salary = salary
        self.project = project

    # method
    def show(self):
        # accessing public data member
        print("Name: ", self.name, 'Salary:', self.salary)

    # method
    def work(self):
        print(self.name, 'is working on', self.project)

emp = Employee('Teja', 18000, 'Python')


emp.show()
emp.work()