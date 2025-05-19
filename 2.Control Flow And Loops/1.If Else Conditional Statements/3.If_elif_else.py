# -----------------------------------------------
# If-Elif-Else Statement in Python
# -----------------------------------------------
# This program checks driving eligibility based on age
# -----------------------------------------------

# Get the user's age as input and convert to integer
age = int(input("Enter your age: "))

# Conditional logic based on age
if age > 18:
    print("You can drive.")                   # Executes if age is greater than 18
elif age == 18:
    print("Let's schedule an interview.")     # Executes if age is exactly 18
else:
    print("Sorry, you cannot drive.")         # Executes if age is less than 18
