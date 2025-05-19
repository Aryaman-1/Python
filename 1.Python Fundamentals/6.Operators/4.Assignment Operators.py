# -----------------------------------------------
# Assignment Operators in Python
# -----------------------------------------------
# These operators combine an operation with assignment.
# -----------------------------------------------

# Initial assignment
a = 35  # '=' assigns the value 35 to variable 'a'
print("value of a:", a)

# += : Add and assign
a += 3  # a = a + 3 → 35 + 3 = 38
print("After a += 3 :", a)

# -= : Subtract and assign
a -= 3  # a = a - 3 → 38 - 3 = 35
print("After a -= 3 :", a)

# *= : Multiply and assign
a *= 3  # a = a * 3 → 35 * 3 = 105
print("After a *= 3 :", a)

# /= : Divide and assign (result will be float)
a /= 3  # a = a / 3 → 105 / 3 = 35.0
print("After a /= 3 :", a)

# %= : Modulus and assign (remainder)
a %= 3  # a = a % 3 → 35.0 % 3 = 2.0
print("After a %= 3 :", a)

# **= : Exponentiation and assign
a **= 3  # a = a ** 3 → 2.0 ** 3 = 8.0
print("After a **= 3:", a)

# //= : Floor divide and assign
a //= 3  # a = a // 3 → 8.0 // 3 = 2.0 (floor division)
print("After a //= 3:", a)
