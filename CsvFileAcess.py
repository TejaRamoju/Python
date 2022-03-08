import csv

class Base:
    def readcsv(self):
        with open("D:\imageswrite.csv","r") as file:
            data=csv.reader(file,delimiter=' ')
            for i in data:
                print(''.join(i))
class Derived(Base):
    def writedata(self):
        with open("D:\imageswrite.csv","w",newline='') as file:
            writer=csv.writer(file)
            writer.writerow(["laptop","240MB","100px","DELL","10","100px"])

    def writemultidata(self,list):
        with open("D:\imageswrite.csv","a",newline='') as file:
            writer=csv.writer(file)
            writer.writerows(list)

d=Derived()
print("data before write")
d.readcsv()
print("data after write(single)")
d.writedata()
d.readcsv()
print("data after write(multiple)")
list=[["laptop","2TB","800px","Dell","09","300px"],["Car","240MB","100px","rose","10","100px"],["xtreme","540MB","500px","Dog","19","100px"]]
d.writemultidata(list)
d.readcsv()
