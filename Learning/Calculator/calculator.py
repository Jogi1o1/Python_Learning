# Calculator function
from diagram import logo

print(logo)
continue_calculation = True

def calculator(first_num):
    """This function is used as a claculator"""
    operator = input("+ \n - \n * \n / \nPick the operation")
    second_num = float(input("Enter the second number!"))
    if operator == "+":
        result = first_num + second_num
        return result
    elif operator == "-":
        result = first_num - second_num
        return result
    elif operator == "*":
        result = first_num * second_num
        return result
    elif operator == "/":
        result = first_num/second_num
        return result

first_num = float(input("Enter the first number!"))
cont = "y"   
while continue_calculation == True:
    if cont == "y":
        first_num = calculator(first_num)
        cont = input(f"Type 'y' to continue calculating with {first_num}, or type 'n' to start a new calculation: ")
        print(cont)
    elif cont == "n":
        first_num = float(input("Enter the first number!"))
        first_num = calculator(first_num)
        cont = input(f"Type 'y' to continue calculating with {first_num}, or type 'n' to start a new calculation, or type 'quit' to stop the calculator: ")
    elif cont == "quit":
        break







