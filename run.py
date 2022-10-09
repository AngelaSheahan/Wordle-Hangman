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


# Wordle-Hangman game introduction
def information():
    game_intro = "Welcome to Wordle-Hangman! As the name implies, all words are of 5\
    letters in length. You, the player, selects a Word Category. The game then\
    randomly selects a word from your chosen category. You then guess what this \
    letter is; 1 letter at a time. Good Luck!"
    game_rules = " 1. Select one of 6 categories.\
    2. The game will randomly generate a word from your choosen category.\
    3. Enter one letter at a time to try to guess this word.\
    4. You have 4 attempts."
    print(game_intro)
    print(game_rules)


# Player selects one of 6 word categories from list of strings pulled from Wordle-Hangman google sheet """
def load_categories():
    global word_categories
    # All category headings appear in row 1 of spreadsheet
    words = wks.row_values(1)
    # Use list comprehension to convert list of lists from google sheet into list of strings"""
    word_categories = [''.join(ele) for ele in words]


def choose_category():
    global choice
    print("Please see list of word categories below:")
    print(word_categories)
    choice = int(input("Enter your choice = "))
    while (choice < 1 or choice >= 7):
        print("This is not a valid category number")
        choice = int(input("Enter your choice = "))
    category = word_categories[choice - 1]
    picked = wks.find(category).value
    print("Your choice is: ",(picked))


def select_random_word():
    global random_word
    word_list = wks.col_values(choice)
    random_word = random.choice(word_list[1:])
    print('The word has' , len(random_word), 'letters')


# Update correct array with correct answers
def update():
    for x in correct:
        print(x, end=' ')
    print()


def wait():
    for i in range(5):
        print('.', end ="")
        sleep(.5)
    print()


# Prepare correct and incorrect variables
def initialise_game():
    global correct
    global incorrect
    information()
    choose_category()
    select_random_word()
    correct = ['_'] * len(random_word)
    incorrect = []

def play_game():
    while True: 
        
        print('############################################')
        guess = input("Guess one letter: ")[0]
        
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
                print("You lose!")
                print("The word was" , random_word)
                break
                
        if '_' not in correct:
            print("You win")
            break


load_categories()
while True:
    initialise_game()
    play_game()
    replay = str(input("Do you want to play again? [y] / [n]: "))
    if replay == 'n':
        print("Goodbye!")
        break