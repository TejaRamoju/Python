'''a = int(input())

if a > 0:
    print("Positive")
else:
    print("Not Positive")

print("End")'''

#Possible mistakes

'''a = int(input())

if a > 0:
    print("Positive")
print("End")

else:
    print("Not Positive")

print("End")'''

#Nested condition

'''matches_won = int(input())

goals = int(input())

if matches_won > 8:

    if goals > 20:
        print("Hurray")
    print("Winner")'''

#Nested Condition in else block


'''a = 2
b = 3
c = 1

is_a_greatest = (a > b) and (a > c)

if is_a_greatest:
    print(a)
else:
    is_b_greatest = (b > c)
    
    if is_b_greatest:
        print(b)

    else:
        print(c)'''


#While Loop

'''a = int(input())

counter = 0

while counter < 3:
    a = a + 1
    print(a)
    counter = counter + 1'''

#1. Missing Initialization

'''a = int(input())

while counter < 3:
    a = a + 1
    print(a)
    counter = counter + 1

print("End")'''



#2. Incorrect Termination Condition
'''a = int(input())
counter = 0
condition = (counter < 3)

while condition:
    a = a + 1
    print(a)
    counter = counter + 1'''
#Infinite Loop

#3. Not Updating Counter Variable

'''a = int(input())
counter = 0

while counter < 3:
    a = a + 1
    print(a)
print("End")'''
#Infinite loop


#For loop sequence of characters

'''word = "Python"

for each_char in word:
    print(each_char)'''

#For loop sequence of numbers
'''a = int(input())
for number in range(a+1):
    print(number)'''

#Nested for loop
for i in range(2):
  print("Outer: " + str(i))#0,1 for 0 itt print(0),1st itt print(1)
  for j in range(2):#0,1 print(0 and 1) print(0,1)
    print(" Inner: " + str(j))