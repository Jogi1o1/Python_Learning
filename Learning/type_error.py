# In this file we are going to under type error
# here TypeError: object of type 'int' has no len() is given in console as len function cannot calculate the length of an integer
print(len(1234))
# here TypeError: can only concatenate str (not "int") to str is given in console as on string can be concatenated to string datatype and same for integer
name_lenth= len(input("What is your name"))
print = ("The length of your name is " + name_lenth + ".")