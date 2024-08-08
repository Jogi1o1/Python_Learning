#default_parameters

# in this function I am defining a default values for both parameter in the case user do not provide the arguments
# non default argument should never follow a default argument for ex (a=1,b) this is a wrong syntax
def calc (a = 1,b =1):
    return (a*b)

# calling function without the arguments
print(calc())

# calling functions with the arguments
print(calc(5,2))
