import gspread
import random
from hangman_parts import bodyParts
from time import sleep
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Wordle-Hangman')
wks = SHEET.worksheet("wordlist")
correct = []
incorrect = []
word_categories = []
choice = 0
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
 

def load_categories():
    """
    The player selects one of 6 word categories from the list of strings (stored in 
    the variable, words) pulled from Wordle-Hangman google sheet. This list consists 
    of the values in row 1 (i.e. the column headings). The Function load_categories 
    pulls the list of categories from the spreadsheet, wordlist. This spreadsheet values
    are assigned to the global variable, wks.
    """
    global word_categories
    # All category headings appear in row 1 of spreadsheet
    words = wks.row_values(1)
    # Use list comprehension to convert list of lists from google sheet into list of strings"""
    word_categories = [''.join(ele) for ele in words]


def choose_category():
    """
    The list of categories is printed to the screen. The player enters their category 
    choice (from 1 to 6). This category choice is stored in the variable picked. Data 
    Validation prevents the player from entering a category below 1 or above 6 or from
    entering a letter instead of a number.
    """
    global choice
    print("Please see list of word categories below:")
    print(word_categories)
    while True:
        try:
            choice = int(input("Enter your choice = \n"))
        except ValueError:
            print("This is not a valid number. Please try again")
            continue
        if (choice < 1) or (choice >= 7):
            print("This is not a valid category number. Please try again")
        else:
            break

    category = word_categories[choice - 1]
    picked = wks.find(category).value
    print("Your choice is: ", (picked))

# or type(choice) != int:

def select_random_word():
    """ 
    The computer randomly selects a word from the category selected by the player.
    This word is stored in the variable, random_word. The word is not displayed to 
    the screen but is represented on the screen in the form of 5 underscores.
    """
    global random_word
    word_list = wks.col_values(choice)
    random_word = random.choice(word_list[1:])
    print('The word has', len(random_word), 'letters')


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
    choose_category()
    select_random_word()
    correct = ['_'] * len(random_word)
    incorrect = []
    player_name = ""

# class play_game:
#     def___init__(self, guess, random_word, correct, incorrect)
#         self.guess = guess
#         self.random_word = random_word
#         self.correct = []
#         self.incorrect = []


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
    load_categories()
    while True:
        initialise_game()
        play_game()
        replay = (input(f"Do you want to play again {player_name}? [y] / [n]: \n"))
        if replay == 'n':
            print(f"Goodbye {player_name}!")
            break


main()
