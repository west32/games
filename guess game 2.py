import random

secret_number = int(input("eneter secret number in range 1-100 "))
guess= random.randint(1,100)
number_of_tries= 1
print(f"CPU: is this {guess}?")
if secret_number == guess:
    print(f"Congratulations! you made it in first shot ! Amazing!")
else:
    upper_range= 100
    lower_range=0
    advice= input("Use advice: 'lower' or 'higher' ")
    while True:
        number_of_tries +=1
        if advice == "lower":
            upper_range = guess -1
        elif advice == "higher":
            lower_range = guess +1
        guess= random.randint(lower_range,upper_range)
        print(f"CPU: is this {guess}?")
        if guess == secret_number:
            print(f" Congratulations! you made it in {number_of_tries} tries ")
            break
        advice=input("")




























