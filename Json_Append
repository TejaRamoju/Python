import json

def appenddata(data,filename="data23.json"):
    with open(filename,"r+") as file:
        content=json.load(file)
        content["employee"].append(data)
        file.seek(0)
        json.dump(content,file,indent=4)


data={
    "id":6,
    "name":"das",
    "department":"Accounts"
}

appenddata(data)
