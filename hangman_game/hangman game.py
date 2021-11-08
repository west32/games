from hangman_game.utilities.random_word_from_file import pick_random_word_from_data
from hangman_game.utilities.guess_the_letter import guessing_logic

def run_game():
   secret_word= pick_random_word_from_data("utilities/sowpods.txt")
   guessing_logic(secret_word)
   play_again=input("play again? (Y/N)").upper()
   while play_again != "N":
       secret_word=pick_random_word_from_data("utilities/sowpods.txt")
       guessing_logic(secret_word)
       play_again=input("play again? (Y/N) ").upper()
   print("GOODBYE!")



if __name__=="__main__":
    run_game()
