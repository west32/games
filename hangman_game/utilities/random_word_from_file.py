import random
def pick_random_word_from_data(file):
    with open(file,"r",encoding='utf=8') as file_txt:
        line= file_txt.readline().strip()
        words = []
        while line:
            words.append(line)
            line=file_txt.readline().strip()
        random_word=random.choice(words)
        return random_word
