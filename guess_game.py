
# moj

secret_number= 9

number_of_tries=0
guess=0
while guess != secret_number and number_of_tries <3:
    guess= int(input("let's guess secret_ number "))
    number_of_tries += 1
    if guess == secret_number:
        print("bravo You Win")
    elif number_of_tries >= 3:
        print("sorry you lost ")

# jego

guess_count= 0
guess_limit =3
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count +=1
    if guess == secret_number:
        print("You Won!")
        break
else:
    print("Sorry you lost ")
