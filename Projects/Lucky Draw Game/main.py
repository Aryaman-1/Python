print("Welcome to the Lucky Draw Entry System")

# Start an infinite loop to allow multiple entries
condition_check=True
while condition_check:
    # Ask user to enter their name
    name = input("Enter your Name: ")
    
    # Ask user to enter their age and convert it to integer
    age = int(input("Enter your age: "))

    # Check if age is less than 18
    if age < 18:
        print("Sry you are not eligible for the lucky draw")
    else:
               # Check if lucky number is greater than 10
        print("You are eligible pls enter your lucky number between 1 and 10", end="")
        lucky_number = int(input(" :"))

        if lucky_number < 10:
            pass
        else:
            print("Your no. is invalid")
            break
                     
            
        # Use match-case to check the lucky number
        match lucky_number:
            case 2:
                print("Congrats you just won a trip to australia")
            case 5:
                print("Congrats you won a 5 dollar gift card")
            case 9:
                print("Congrats you just won a brand new mobile phone")
            case _:
                print("Better Luck Next Time!!!!")
                # If number is not 2, 5, or 9

    # Ask if user wants to try again
    print("Would you like to try again", "1-Yes", "2-No")
    option = int(input("Choose yes or no: "))

    # If user chooses 2, end the program
    if option == 2:
        print("Thank you for participating Bye")
        break
        condition_check=False
    # If user chooses 1, continue the loop
    elif option == 1:
        print("Try Again")
        continue
    # If user enters an invalid option, exit with message
    else:
        print("Invalid Number")
        condition_check=False

        
        