# -----------------------------------------------
# Loop Control Statements in Python
# -----------------------------------------------

# ----------- BREAK -----------
print("Demonstrating 'break':")
for i in range(1, 20):
    print(i)
    if i == 11:
        break  # Exits the loop completely when i is 11

# ----------- CONTINUE -----------
print("\nDemonstrating 'continue':")
for i in range(1, 20):
    if i == 10:
        continue  # Skips the rest of this loop iteration when i is 10
    print(i)       # This line is skipped only when i == 10

# ----------- PASS -----------
# 'pass' is a placeholder used when a statement is required due to syntax but you dont want any code to run yet
print("\nDemonstrating 'pass':")
i = 3
if i == 3:
    pass  # Do nothing for now (used as a placeholder)

print("End of program")
