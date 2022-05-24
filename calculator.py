def add(num1, num2):

    return num1 + num2

def subtract(num1, num2):

    return num1 - num2

def multipy(num1, num2):

    return num1 * num2

def divide(num1, num2):

    return num1 / num2

def modulus(num1, num2):

    return num1 % num2

print("what tpye of calculation do you want to do?\nreply with:")

print("add : for addition,\nsub : for subtraction\nmul : for multipication\ndiv : for division\nrem : for reminder")

fun =input()

first_dig = int(input(" First digit(s)\n\n"))

second_dig = int(input(" Second digit(s)\n\n"))

result = 0

if fun == "add":
    result = add(first_dig, second_dig)

elif fun == "sub":
    result = subtract(first_dig, second_dig)

elif fun == "mul":
    result = multipy(first_dig, second_dig)

elif fun == "div":
    result = divide(first_dig, second_dig) 

elif fun == "rem":
    result = modulus(first_dig, second_dig)

else:
    print("your functions is not defined")

print(f'{first_dig}  {fun} {second_dig} = {result}' )