class school :


    a = "student"

    def __init__(self, name, age,grade):
        self.name = name
        self.age = age
        self.grade = grade
        print(self.grade)

b = school("Raghav", 10,"79%")
c = school("Teja", 15,"83%")


print("Raghav is a {}".format(b.__class__.a))
print("Teja is also a {}".format(c.__class__.a))

print("{} is {} years old".format(b.name, b.age))
print("{} is {} years old".format(c.name, c.age))

print("{} scored {} in Final Exams".format(b.name, b.grade))
print("{} scored {} in Final Exams".format(c.name, c.grade))