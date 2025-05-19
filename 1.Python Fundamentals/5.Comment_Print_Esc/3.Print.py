# -----------------------------------------------
# The print() Function in Python
# -----------------------------------------------

# By default, print separates items with a space
print("Hello, how are you?", "Fine", "Thank you")  # Output: Hello, how are you? Fine Thank you

# Using 'sep' to customize the separator between items
print("Hello my name is Aryaman", "Age is 14", "Interested in Python", sep=" , ")
# Output: Hello my name is Aryaman , Age is 14 , Interested in Python

# -----------------------------------------------
# Controlling End of Line in print()
# -----------------------------------------------

print('Hello Aryaman')  # Newline by default
print('How are you?')

# Using  'end' to control what gets printed after the print statement
print('Hello, Im good', end=" , ")      # Ends with a comma instead of newline
print('What about you?', end=" // ")     # Adds custom ending

# Output:
# Hello, I’m good , What about you? //