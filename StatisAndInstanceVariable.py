class StaticVariable:
    staticVariable=8

    def __init__(self):
        self.instance_a=20
        self.instance_b=30

s=StaticVariable()
print("Static variable using className ",StaticVariable.staticVariable)
print("Static variable using object ",s.staticVariable)
print("instance a using object ",s.instance_a)
print("instance b using object ",s.instance_b)


s.staticVariable=19

print("Static variable using object",s.staticVariable)
print("Static variable using className",StaticVariable.staticVariable)

StaticVariable.staticVariable=15
print("Static variable using className",StaticVariable.staticVariable)
print("Static variable using object",s.staticVariable)