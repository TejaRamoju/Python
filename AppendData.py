import json

# Data to be written
dictionary ={
         "id": "09",
         "name": "Virat",
         "department": "Sports"
      }

with open("data.json", "a") as outfile:
   json.dump(dictionary, outfile,indent=4)
