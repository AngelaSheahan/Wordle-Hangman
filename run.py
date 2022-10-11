
from time import sleep
from dictionary import Dictionary

correct = []
incorrect = []
random_word = ""


def information():
    """
    This game is called, Wordle-Hangman, combining the New York Times hugely successful,
    daily 5 letter guessing game, Wordle, and the traditional game, Hangman.
    When this function is called, it displays a game introduction and the game rules to
    the screen
    """
    game_intro = "Welcome to WORDLE HANGMAN! This is a 5 letter guessing game.\nGOOD LUCK!"
    game_rules = "1. Select one of 6 categories.\n2. The game will randomly generate a word from your choosen category.\n3. Enter one letter at a time to try to guess this word.\n4. You have 4 attempts.\n"
    print("---------------------------------------------------------------")
    print(game_intro)
    print(game_rules)
    print("----------------------------------------------------------------")
    global player_name
    player_name = input("Please enter your name:  \n")
    print("Welcome " + player_name)
    print("-----------------------------------------------------------------")


# Update correct list with correct answers
def update():
    """
    Add correct guesses to the correct list. The end=' ' is added here to ensure that each
    correct letter is added beside each other in list, not on separate lines.
    """
    for x in correct:
        print(x, end=' ')
    print()


def wait():
    """
    Python time sleep() function suspends execution for 5 seconds. This I use to
    build up suspension in the game after a player makes a guess. There is a 5 second
    delay before the result (i.e. is the players guess correct or incorrect?) is displayed.

    """

    for i in range(5):
        print('.', end=" ")
        sleep(.5)
    print()


def initialise_game():
    """
   When player chooses to play again, the correct and incorrect lists are cleared out.
   The choose_category(), and select_random_word() funcions are called.
    """
    global correct
    global incorrect
    correct = ['_'] * len(random_word)
    incorrect = []
    player_name = ""




def main():
    information()
    myDictionary = Dictionary()
    while True:
        global random_word
        random_word = myDictionary.select_random_word()
        initialise_game()
        play_game()
        replay = (input(f"Do you want to play again {player_name}? [y] / [n]: \n"))
        if replay == 'n':
            print(f"Goodbye {player_name}!")
            break


main()

