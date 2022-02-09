class DefaultConstructor:
    def __init__(self):
        self.name="default"
        print("default constructor : ",self.name)


class ParametraisedConstructor:
    def __init__(self,name):
        self.name=name


    def __del__(self):
        print("Deleted")

    def display(self):
        print("parametraised constructor : {}".format(self.name))

cons =DefaultConstructor()
para =ParametraisedConstructor("Teja")
para.display()