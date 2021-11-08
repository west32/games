# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number,
# then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons
# from the very first exercise)
#
# Extras:
#
# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random
secret_number= random.randint(1,9)
answear = 0
number_of_tries= 0
while answear != secret_number:
    answear=int(input("Please guess secret number 1-9: "))
    number_of_tries += 1
    if answear < secret_number:
        print("I think secret number it's a bit higher")
    elif answear > secret_number:
        print("Secret number its a bit lower... try again")
    else:
        print(f"Congratulations You made it in {number_of_tries} tries!")