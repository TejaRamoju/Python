import json

addr='{"city":"Hyderabad","state":"Telangan","country":"india"}'
pin={"pincode":100119}

fulladr=json.loads(addr)
fulladr.update(pin)

print(fulladr)
