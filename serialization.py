import json
var = {
      "Virat": {
                  "Maths":85,
                  "English":90,
                  "Hindi":100
                   },
"Abd": {
                  "Maths":90,
                  "English":95,
                  "Hindi":100
                   }
      }
with open("arraySample.json", "w") as p:
 json.dump(var, p)
