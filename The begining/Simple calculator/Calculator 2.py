# addition function
def addition(a, b):
    return a + b

# subtraction function
def subtraction(a, b):
    return a - b

# multiplication function
def multiplication(a, b):
    return a * b

# division function
def division(a, b):
    return a / b


#Prompt the user once for the two numbers and store them in variables
a = int(input ("What is the first number? "))
b = int(input ("What is the second number? "))

# Prompt the user for input
user_input = input("What type of calculation do you want today? addition, subtraction, multiplication, or division: ")

# Check the user's input and run a specific if statement based on the input
if user_input == "addition":
    print("Result:", addition(a, b))

elif user_input == "subtraction":
    print("Result:", subtraction(a, b))

elif user_input == "multiplication":
    print("Result:", multiplication(a, b))

elif user_input == "division":
    print("Result:", division(a, b))

else:
    print("Check your spelling please ")