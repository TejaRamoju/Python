import csv
data=[["id","name","age"],["100", "Virat", "18"],["101", "Abd", "21"]]
with open("D:\writemultipledemo.csv",'w',newline='') as file:
    writer1=csv.writer(file)
    writer1.writerows(data)
