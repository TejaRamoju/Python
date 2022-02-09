class Base:
    def base(self):
        print("base class")
class Base2:
    def base2(self):
        print("base 2")
class Child(Base):
    def child(self):
        print("child")

class SubChild(Child):
    def subchild(self):
        print("SubChild")

class Multiple(Child,Base):
    def multiple(self):
        print("Multiple")

base = Base()
base.base()
child_ =Child()
child_.base()
child_.child()
sub_child=SubChild()
sub_child.base()
sub_child.child()
sub_child.subchild()
Multi =Multiple()
Multi.multiple()