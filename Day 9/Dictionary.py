dict1 = {"name": "Udit Gupta", "age": 27, "address": "Indore"}
# Access dictionary item
print(dict1["name"])

# Get Dictionary Values and Keys
print(dict1.values())
print(dict1.keys())

# Empty String
my_dict = {}
print(my_dict)

# Wipe the dict
dict1 = {}
print(dict1)

# Add an Item to Dict
dict1["pincode"] = 453771
print(dict1)

# Edit an Item in Dict
dict1["pincode"] = "453771"
print(dict1)

print("------------Looping---------")
# Looping through Dict
for key in dict1:
    print(key)
for values in dict1.values():
    print(values)
for keys in dict1.keys():
    print(keys)

for key in dict1:
    print(key)
    print(dict1[key])
