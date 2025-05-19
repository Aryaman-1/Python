# --------------------------
# Typecasting in Python
# --------------------------

# Original variables of different types
string_number = "34"     # String that looks like a number
integer_value = 300      # Integer
float_value = 2.5        # Float (decimal)

# Display original values and their types
print(string_number)
print("Type of string_number:", type(string_number))  # <class 'str'>

print(integer_value)
print("Type of integer_value:", type(integer_value))  # <class 'int'>

print(float_value)
print("Type of float_value:", type(float_value))      # <class 'float'>


# --------------------------
# Typecasting Examples
# --------------------------

# Convert string_number (str) to integer
converted_int = int(string_number)
print(converted_int)
print("Type of converted_int:", type(converted_int))  # <class 'int'>


# Convert integer_value (int) to string
converted_str = str(integer_value)
print(converted_str)
print("Type of converted_str:", type(converted_str))  # <class 'str'>


# Convert float_value (float) to integer (fractional part is truncated)
converted_from_float = int(float_value)
print(converted_from_float)
print("Type of converted_from_float:", type(converted_from_float))  # <class 'int'>
