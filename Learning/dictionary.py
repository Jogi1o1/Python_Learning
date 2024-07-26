# Dictionary

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again."
}

# printing the value of a key
#print(programming_dictionary["Bug"])

# adding a new key:value pair
programming_dictionary["Loop"] = "Iteration"

# editing the value of a key
programming_dictionary["Bug"] = "hell"

# creating an empty dictionary
empty_dictionary = {}

for key in programming_dictionary:
    print(f"{key} : {programming_dictionary[key]}")

