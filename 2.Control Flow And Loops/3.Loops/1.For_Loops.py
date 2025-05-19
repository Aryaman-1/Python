# -----------------------------------------------
# Using For Loops and the range() Function
# -----------------------------------------------

# Example: Manually printing numbers (not scalable)
# print(1)
# print(2)
# print(3)
# print(4)
# print(5)

# Looping from 1 to 5 using range(start, stop)
# Note: range(1, 6) includes 1 but excludes 6
print("Numbers from 1 to 5:")
for i in range(1, 6):
    print(i)

# -----------------------------------------------

# Example: Printing the multiplication table of 5
print("\nMultiplication Table of 5:")
for i in range(1, 11):  # Loops from 1 to 10
    print("5 x ",i," = ",5 * i)
    # In each loop cycle, the variable 'i' takes one number from the range (1 to 10)
    # It starts at 1, then 2, then 3, and so on — up to 10
    # We use 'i' in the print statement to calculate and show: 5 * i
