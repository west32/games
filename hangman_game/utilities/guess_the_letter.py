def guessing_logic(secret_word):
    secret_word= secret_word
    print("Welcome in Hangman Game!")
    listone=[]
    guessed_list=[]
    hidden_word= ""

    for _ in range(len(secret_word)):
        listone.append("_")
    for element in listone:
        hidden_word +=f" {element}"

    print(hidden_word)
    incorrect_counter=6
    while True:

        listtwo = []
        guess=input("Guess the letter: ").upper()
        if guess in guessed_list:
            print("You have already tried this one")
        else:
            guessed_list.append(guess)

            if guess in secret_word:
                for letter in secret_word:
                    if guess== letter:
                        listtwo.append(letter)
                    else:
                        listtwo.append("_")
                for index, element in enumerate(listone):

                    if element != listtwo[index] and element == "_":
                        listone[index] = listtwo[index]

            else:
                print("Incorrect!")
                incorrect_counter -=1
                if incorrect_counter ==0:
                    print(f"Game Over\n secret word={secret_word}")
                    print("""                             |-----------
                             |          |   
                             O          |
                            |[]|        |
                             ||         |
                                    ____|____""")
                    break
                print(f" You can eneter {incorrect_counter} more incorrect answers")
                if incorrect_counter ==5:
                    print("""                             |-----------
                             |          |   
                             O          |
                                        |
                                    ____|____""")
                elif incorrect_counter ==4:
                    print("""         |-----------
                             |          |   
                             O          |
                             []         |
                                        |
                                    ____|____""")
                elif incorrect_counter ==3:
                    print("""                             |-----------
                             |          |   
                             O          |
                            |[]         |
                                        |
                                    ____|____""")
                elif incorrect_counter ==2:
                    print("""                             |-----------
                             |          |   
                             O          |
                            |[]|        |
                                        |
                                    ____|____""")

                elif incorrect_counter ==1:
                    print("""                             |-----------
                             |          |   
                             O          |
                            |[]|        |
                             |          |
                                    ____|____""")

        hidden_word=""
        for element in listone:
            hidden_word += f" {element}"
        print(hidden_word)
        if "_" not in listone:
            print(f"Congtatulations")
            break

