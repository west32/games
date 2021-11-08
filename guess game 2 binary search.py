import random
secret_number = int(input("set your secret number 1-100 "))



number_of_tries=0
guess = 50
print(f" CPU: is it {guess}?")
if guess == secret_number:
    print("Congratulations! You made it in 1st shot!")
else:
    min_range = 0
    max_range = 100
    advice = input("Use advice 'lower' or 'up' ")
    while True:

        number_of_tries +=1

        if advice == "lower":
            max_range=guess -1
        elif advice=="up":
            min_range=guess +1
        mid = (max_range + min_range) / 2
        guess=round(mid)
        print(f"CPU: is that {guess}?")
        if guess == secret_number:
            print(f"Congratulations! You made it in {number_of_tries} tries")
            break
        advice = input("")