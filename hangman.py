import random

#Sample words to be chosen from
words = ["ketchup", "milk", "computer", "python", "dog", "superior", "dynamic", "duo"]

class game:
    def __init__(self):
        self.lives = 6
        self.guessed = []
        #Selects a random word from array
        self.word = random.choice(words)
        self.word_array = []
        for x in self.word:
            self.word_array.append(x)
        self.status = True
    def guess(self, g):
        if len(g) == 1:
            if g in self.guessed:
                print("You already guessed this letter.")
            else:
                self.guessed.append(g.lower())
                if g.lower() in self.word_array:
                    print(g + " was in the word")
                else:
                    self.lives -= 1
                    print(g + " was not in the word :(\n" + str(self.lives) + " lives remaining ;-;")
                    if self.lives == 5:
                        print("     _\|/^\n      (_oo")
                    elif self.lives == 4:
                        print("     _\|/^\n      (_oo\n       |\n       |\n       |")
                    elif self.lives == 3:
                        print("     _\|/^\n      (_oo\n       |\n      \|\n       |")
                    elif self.lives == 2:
                        print("     _\|/^\n      (_oo\n       |\n      \|/ \n       |")
                    elif self.lives == 1:
                        print("     _\|/^\n      (_oo\n       |\n      \|/ \n       |\n       L")
                    elif self.lives == 0:
                        print("     _\|/^\n      (_xx\n       |\n      \|/ \n       |\n       LL")
                        self.status = False
                        print("You ran out of lives :(")
        else:
            print("Please only input one letter")

start = input("Do you want to play Hangman? (y or n)\n")
if start.lower() == "y":
    #starts Hangman game
    new_game = game()
    while(new_game.status):
        word_view = ""
        for x in new_game.word_array:
            if x.lower() not in new_game.guessed:
                word_view += "_ "
            else:
                word_view += x.upper() + " "
        if "_" in word_view:
            print(word_view)
            user_guess = input("Guess a Letter:\n")
            new_game.guess(user_guess)
        else:
            new_game.status = False
            print("The word was " + new_game.word + "!")
else:
    print("Okie goodbye!")
