# You are going to write a program that will mark a spot with an X.

# In the starting code, you will find a variable called map.

# This map contains a nested list. When map is printed this is what the nested list looks like:

# [['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]

# Creating 3 different list
row1 = ['⬜️', '⬜️', '⬜️']
row2 = ['⬜️', '⬜️', '⬜️']
row3 = ['⬜️', '⬜️', '⬜️']
# Concatenating all lists in a single list
map = [row1,row2,row3]
# printing all rows
print(f"{row1},\n{row2},\n{row3}\n")
# taking input from the user where they want to put their treasure in 2d array
position = input("Where do you want to place the treasure?\n")
# now we are storing the input at 0th index as uppercase
capital = position[0].upper()
# now we are creating a new list for the comparison puposes of our input
new_list = ["A", "B", "C"]
# now we are finding the index of the character by comparing the input item to the newly added list
letter_index = new_list.index(capital)
# now we are finding the index of column by separating the number from alphabet in the string
num_index = int(position[1]) - 1
# now we are replacing the value of box to X in the map 
map[letter_index][num_index] = "X"
# now we are printing the result
print(f"{row1},\n{row2},\n{row3}\n")