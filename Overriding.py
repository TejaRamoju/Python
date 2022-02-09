class Base:
    def x(self):
        print("Parent Class")

class Child(Base):
    def x(self):
        super(Child,self).x()
        print("child class")

y=Child()
y.x()