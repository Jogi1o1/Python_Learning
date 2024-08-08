#dictionaries_functions

# declaring a dict
dict = {
    "name" : "Jogi",
    "cgpa" : 9.6,
    "marks" : [98,97,95]
}

# calculating the length of dict
print(len(dict))

# getting all the values from the dict
print(dict)

# getting a specific value from the dict
print(dict["marks"][0])

# changing the value of any key in dict
dict["name"] = "Joginder"
print(dict["name"])

# adding new object into the dictionary
dict["surname"] = "Singh"
print(dict)

# nested dictionaries
students = {
    "name" : "Jogi",
    "subjects" : {
        "phy" : 97,
        "maths" : 98,
        "chem" : 95
    },
    "cgpa" : 9.6
}

print(students["subjects"]["phy"])

# dict.keys() will return all the keys that are present in the dictionaries in the form of list
print(students.keys())
print(students["subjects"].keys())

#dict.values() will return values of all keys that are present in the dictionaries in the form of list
print(students.values())
print(students["subjects"].values())

#dict.itmes() return all keys and values as tuple
print(students.items())
print(students["subjects"].items())

#dict.get("key") return the value that have the specified key
print(students.get("cgpa"))
print(students["subjects"].get("chem"))

#dict.update({"key" : "value"}) enters the new specified key value pair in dictionary
dict.update({"name" : "Jogi"})
print(dict)

