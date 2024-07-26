# Modify the global variable inside any function

name = 'Joginder Singh'
def my_name():
    global name
    name = 'Jogi'

my_name()
print(name)
print(helo)

# As the variable value is changed in the function using 'global' keyword than the value is changed globally not only locally