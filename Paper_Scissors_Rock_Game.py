# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for
# player plays (using input), compare them, print out a message of
# congratulations to the winner, and ask if the players want to start a new game)
#
# Remember the rules:
#
# Rock beats scissors
# Scissors beats paper
# Paper beats rock
def welcome():
    print("""
    Welcome in Rock, Paper, Scissors Game 
    
    """)
    player1_name = str(input("what is player 1 name? "))
    player2_name = str(input("what is player 2 name? "))
    return player1_name, player2_name

def start_game(player1_name,player2_name):
    while True:
        player1_answer = input(f"{player1_name} please make a choice Rock/Paper/Scissors ").title()
        player2_answer = input(f"{player2_name} please make a choice Rock/Paper/Scissors ").title()

        if player1_answer == player2_answer:
            print("its a tie, make a choice again!")
        if player1_answer == "Rock":
            if player2_answer == "Paper":
                print(f"Paper beats Rocks {player2_name} Won! Congratulations!")
                break
            elif player2_answer == "Scissors":
                print (f"Rock beats Scissors {player1_name} Won! Congratulations!")
                break
        elif player1_answer == "Paper":
            if player2_answer == "Scissors":
                print(f"Scissors beats Paper {player2_name} Won! Congratulations!")
                break
            elif player2_answer == "Rock":
                print(f"Paper beats Rock {player1_name} Won! Congratulations!")
                break
        elif player1_answer == "Scissors":
            if player2_answer == "Rock":
                print(f"Rock beats Scissors {player2_name} Won! Congratulations!" )
                break
            elif player2_answer == "Paper":
                print(f"Paper beats Rock {player2_name} Won, Congratulations!")
                break
        else:
            print("there is only 3 options to make: Paper/ Scissors / Rock")

def ask_for_another_game():
    option= ""
    option= str(input("Do you want to play one more time? Y/N")).upper()
    return option

def run_example():

    player1_name, player2_name = welcome()
    start_game(player1_name,player2_name)
    answear = ask_for_another_game()
    while answear != "N":
        start_game(player1_name,player2_name)
        answear = ask_for_another_game()

if __name__ =="__main__":
    run_example()