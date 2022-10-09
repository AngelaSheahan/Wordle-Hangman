# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
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



# Wordle-Hangman game introduction
# def intro_rules():
#     game_intro = "Welcome to Wordle-Hangman! As the name implies, all words are of 5\
#     letters in length. You, the player, selects a Word Category. The game then\
#     randomly selects a word from your chosen category. You then guess what this \
#     letter is; 1 letter at a time. Good Luck!"
#     game_rules = " 1. Select one of 6 categories.\
#     2. The game will randomly generate a word from your choosen category.\
#     3. Enter one letter at a time to try to guess this word.\
#     4. You have 4 attempts."\
#     print(game_intro)
#     print(game_rules)


# Player selects one of 6 word categories from list of strings pulled from Wordle-Hangman google sheet """
def categories():
    print("Please see list of word categories below:")
    # All category headings appear in row 1 of spreadsheet
    wks = SHEET.worksheet("wordlist")
    words = wks.row_values(1)
    # Use list comprehension to convert list of lists from google sheet into list of strings"""
    word_categories = [''.join(ele) for ele in words]
    print(word_categories)


def choose_category():
    choice = int(input("Enter your choice = "))
    while (choice < 1 or choice >= 7):
        print("This is not a valid category number")
        choice = int(input("Enter your choice = "))
    category = word_categories[choice - 1]
    picked = SHEET.worksheet("wordlist").find(category).value
    print("Your choice is: ",(picked))
    word_list = wks.col_values(choice)
    random_word = random.choice(word_list[1:])
    return (random_word)

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


# Function to enable player the option of exiting the game or playing a new game
def new_game_exit():
    playagain = str(input("Do you want to play again? [y] / [n]: "))
    if playagain == 'y':
        initialise_game()
        choose_category()
       
    else:
        print("Goodbye!")


# Prepare correct and incorrect variables
def initialise_game():
    random_word = choose_category()
    print('The word has' , len(random_word), 'letters')
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
                index +=1
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
            
                new_game_exit()
                
        if '_' not in correct:
            
            print("You win")
            
            new_game_exit()



# Funtion Calls 

# intro_rules()

categories()

choose_category()

update()

wait()

play_game()

initialise_game()


