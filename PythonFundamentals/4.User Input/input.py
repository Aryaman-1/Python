# ---------------------------------------
# Taking Input from the User in Python
# ---------------------------------------

# Basic Input: Reads input as a string by default
# Uncomment below to test simple input and print
number_input = input("Enter a number: ")
print("You entered:", number_input)

name_input = input("Enter your name: ")
print("Hello", name_input)

# ---------------------------------------
# Input with Typecasting: String → Integer
# ---------------------------------------

# Taking a number input and converting it to integer
number = input("Enter a number: ")
number = int(number)  # Typecasting from string to integer
print("Number + 3 =", number + 3)  # Adds 3 to the number and prints it

# ---------------------------------------
# Adding Two Numbers from User Input
# ---------------------------------------

# Taking first number input
first_number = int(input("Enter the first number: "))  # Directly cast input to int

# Taking second number input
second_number = int(input("Enter the second number: "))  # Directly cast input to int

# Performing addition
sum_result = first_number + second_number
print("Sum of the numbers:", sum_result)
