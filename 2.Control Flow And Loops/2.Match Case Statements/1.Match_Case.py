# -----------------------------------------------
# Match-Case Statement in Python (Python 3.10+)
# -----------------------------------------------
# This program rewards users based on their lucky number input.
# -----------------------------------------------

# Ask the user for a lucky number between 1 and 10
a = int(input("Enter a lucky number between 1 and 10: "))

# Match-case is used like a switch-case statement
match a:
    case 1:
        print("🎁 You won a charger!")
    case 3:
        print("💵 You won $3!")
    case 7:
        print("💻 You won a laptop!")
    case _:  # Default case (if no match)
        print("😢 Better luck next time.")
