# -----------------------------------------------
# While Loops in Python
# -----------------------------------------------

# Example: Manually printing numbers (not scalable)
# print(1)
# print(2)
# print(3)
# print(4)
# print(5)

# -----------------------------------------------
# Using a while loop to print numbers from 1 to 5
print("Printing numbers from 1 to 5 using while loop:")

i = 1 
while i < 6:
    print(i)
    i += 1  # Increment 'i' to eventually break the loop

# -----------------------------------------------
# Infinite Loop Example (⚠️ use with caution!)
# This loop will run forever unless manually stopped
# Uncomment the lines below to see how it works

# print("\nStarting infinite loop:")
# while True:
#     print(i)
#     i += 1
