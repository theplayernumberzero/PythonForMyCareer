#Instead of writing complex data directly, we will do serialization
#data turns stream in serialization

#turning Python dictionary to JSON object

import json

data = {
    "name" : "Bahadir",
    "age": 23,
    "city": "Sivas"
}

json_data = json.dumps(data)    #turns dictionary to Json object

print(type(data))
print(type(json_data))  #str

#Deserialization: Json object to dictionary

json_data2 = '{"name" : "Bahadir","age": 23,"city": "Sivas"}'

data2 = json.loads(json_data2)

print(type(data2))
print(type(json_data2))
print(data2["name"])