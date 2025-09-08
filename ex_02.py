# odd or even
# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.


# Extra 01: If the number is a multiple of 4, print out a different message.

# get user input
int_num = int(input("Enter a number: "));

# check for odd or even
if int_num % 2 == 0:
    # Extra 01
    if int_num % 4 == 0:
        print(f"{int_num} is divisible by 4!");
    else:
        print(f"{int_num} is an even number");
else:
    print(f"{int_num} is an odd number");   
    
# Extra 02: Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
check = int(input("Enter a number to check:"))

# If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
if int_num / check % 2 == 0 or int_num / check % 2 == 1:
    print(f"{check} divides evenly into {int_num}");
else:
    print(f"{check} doesn't divided into {int_num}");







    
    
    

