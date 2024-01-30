# List are used to store connected data
# Items are stored in the list with their index
List_of_fruits = ["Apple", "Mango", "Orange", "Pomergranate", "Pear"]
# Items in list can be fetched after adding the square bracket at the end of variable and providing the index of that variable after that.
print(List_of_fruits[4])
# Items can also be fetched using negative index also i.e. they will start fetching data from the end of the not from start
print(List_of_fruits[-2])
# Items can also be replaced just by adding a new item in the index of older one for e.g.
List_of_fruits[2] = "Papaya"
print(List_of_fruits)
# We can also add an item at the end of the list using append function
List_of_fruits.append("Water Melon")
# Now we print the new list
print(List_of_fruits)
# We can also add the list if items to the list
List_of_fruits.extend(["Avacado", "Grapes", "Blueberry"])
# printing the list
print(List_of_fruits)