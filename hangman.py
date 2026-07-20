import random
#If statements
#functions
#inputs
#Strings
#loops
#consequence
#Use madlibs to help


#def main(word,correctlttr1,correctlttr2,correctlttr3,correctlttr4,correctlttr5,correctlttr6,correctlttr7,correctlttr8):
    #word = "Birthday"
    #correctlttr1 = "B"
    #correctlttr2 = "i"
    #correctlttr3 = "r"
    #correctlttr4 = "t"
    #correctlttr5 = "h"
    #correctlttr6 = "d"
    #correctlttr7 = "a"
    #correctlttr8 = "y"







#def choice(seq):
    
#Letter = input("Please enter a letter")
#list(random_word)


#for i, correct_letter in range(random_word):
    #while True:
        #Letter



    
def display_word():
    for letter in random_word:
        if letter in letters_guessed:
            print(letter, end="")
        else:
            print("_", end="")

    
def guessed_word(letter,random_word,):
    if letter == random_word:
        display_word()
        letters_guessed.append(letter)
        print("You guessed the letter correctly!!!")
        print(Guess)
    elif letter != random_word:
        lives -= 1
    return guessed_word


def main():
    print("Welcome to hangman we will have your word shortly")
    words = ['Birthday','Restaurant','Sevant','Murderer']
    random_word = random.choice([words])
    letters_guessed = []
    lives = 10

    while lives >= 0:
        Guess = input("Guess a letter")
    display_word()
    guessed_word()
    if letters_guessed == random_word and lives != 0:
        print("You won!")
    elif lives == 0:
        print("You lost!")
        main()














    #def main():
        #display_word = print()
        





    




