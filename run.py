from hangman_parts import bodyParts
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


def play_game():
    """
    Run a while loop to collect an input(a guess) from the user via the terminal,
    which cannot be a number. All correct letter guesses will fill the appropriate
    underscore slot in the 'correct' list; incorrect letter guesses are be added 
    to the 'incorrect' list and also displayed on screen. When the player makes
    either 1, 2, 3, or 4 incorrect guesses, the bodyParts function is called (which is stored
    in another file called hangman_parts.py), displaying either the head, body, arms, and legs! 
    The loop will repeatedly request data, until all the underscores are replaced 
    by words (i.e. all the correct letters have been guessed), or the incorrect list is > 4.
    (as all random words are 5 letters in length)
    Run a second While loop in the event that the player wishes to play again. The initialise_game()
    function is called to clear the variable contents.
    """

    while True:

        print("-----------------------------------------------------------------")
        guess = input("Guess one letter: \n")[0]

        if guess.isnumeric():
            print("Enter a letter not a number: ")
            continue

        if guess in random_word:
            index = 0
            for x in random_word:
                if x == guess:
                    correct[index] = guess
                index += 1
            update()

        else:
            if guess not in incorrect:
                incorrect.append(guess)
                bodyParts(len(incorrect))
            else:
                print("You have already guessed that")
            print(incorrect)
            if len(incorrect) > 4:
                print(f"You lose {player_name}!")
                print("The word was", random_word)
                break
        if '_' not in correct:
            print(f"You win {player_name}")
            break

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

