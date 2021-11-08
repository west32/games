import random

def welcome():
    name= input("What's your name? >>>")
    print(f"{name} Welcome to the Cows and Bulls game!")
    return name

def generate_secret_number():
    secret_number = ""
    for _ in range (4):
        number= random.randint(0,9)
        secret_number += str(number)
    return secret_number

def game (secret_number, name):
    number_of_tries= 0
    while True:
        number_of_tries +=1
        guess = input(
""" Enter 4-digits number
>>>""")
        if len(guess) > 4:
            print(f"4-digits number...it's not {len(guess)}- digit number ")
            continue
        number_of_cows= 0
        number_of_bulls=0
        if guess == secret_number:
            if number_of_tries == 1:
                print(f"Conratulation {name}, your answer correctly in 1st try! the number it's {secret_number}")
                break
            else:
                print(f"Conratulation {name}, your answer correctly in {number_of_tries} tries! the number it's {secret_number}")
                break
        for index,number in enumerate(guess):
            a= number
            a_index = index
            if a in secret_number:
                for index, number in enumerate(secret_number):
                    b= number
                    b_index= index
                    if a==b and  a_index == b_index:
                        number_of_cows +=1

                    elif a==b and a_index != b_index:
                        number_of_bulls +=1



        print(f"cows:{number_of_cows}, bulls: {number_of_bulls}")

def run_game():
    name= welcome()
    secret_number= generate_secret_number()
    game(secret_number,name)






if __name__=="__main__":
    run_game()