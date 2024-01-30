# You are going to write a program that will mark a spot with an X.

# In the starting code, you will find a variable called map.

# This map contains a nested list. When map is printed this is what the nested list looks like:

# [['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]

# Creating 3 different list
row1 = ['⬜️', '⬜️', '⬜️']
row2 = ['⬜️', '⬜️', '⬜️']
row3 = ['⬜️', '⬜️', '⬜️']

# printing all rows
print(f"{row1},\n{row2},\n{row3}\n")
# taking input from the user where they want to put their treasure in 2d array
treasure_place = input("Where do you want to place the treasure?\n")
var_1 = int(treasure_place[0])
var_2 = int(treasure_place[1])
if var_1 == 1 :
  if var_2 == 1 :
    row1[0] = 'X'
    print(f"{row1},\n{row2},\n{row3}\n")
  elif var_2 == 2 :
    row1[1] = 'X'
    print(f"{row1},\n{row2},\n{row3}\n")
  else :
    row1[2] = 'X'
    print(f"{row1},\n{row2},\n{row3}\n")
elif var_1 == 2 :
  if var_2 == 1 :
    row2[0] = 'X'
    print(f"{row1},\n{row2},\n{row3}\n")
  elif var_2 == 2:
    row2[1] = 'X'
    print(f"{row1},\n{row2},\n{row3}\n")
  else :
    row2[2] = 'X'
    print(f"{row1},\n{row2},\n{row3}\n")
else :
  if var_2 == 1 :
    row3[0] = 'X'
    print(f"{row1},\n{row2},\n{row3}\n")
  elif var_2 == 2 :
    row3[1] = 'X'
    print(f"{row1},\n{row2},\n{row3}\n")
  else :
    row3[2] = 'X'
    print(f"{row1},\n{row2},\n{row3}\n")
