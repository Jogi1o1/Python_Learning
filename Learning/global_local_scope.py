#Scope

# Local Scope
# def my_name():
#     name = 'Joginder Singh'
#     print(name)

# my_name()
# print(name)
# Here the variable name is defined inside a function so it can only be accessed inside the function

# Global Scope
name = 'Joginder Singh'
def my_name():
    name =  'Jogi'
    print(name)

my_name()
print(name)