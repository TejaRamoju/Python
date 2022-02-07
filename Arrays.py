import array
a = array.array('i',[1,2,3,4,5])
for i in a:
    print(i,end = " ")
x = []
for i in range(len(a)):
    x.append(a[i])
print(x)
print(a)
a.remove(1)
print(a)
a.pop()
print(a)
a.insert(2,8)
print(a)
a.append(7)
print(a)
print("maximum value",max(a))
print("minimum value",min(a))
