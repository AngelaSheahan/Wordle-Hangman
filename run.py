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
game_intro = "Welcome to Wordle-Hangman! As the name implies, all words are of 5\
    letters in length. You, the player, selects a Word Category. The game then\
    randomly selects a word from your chosen category. You then guess what this \
    letter is; 1 letter at a time. Good Luck!" 

print(game_intro)  

# Display game rules
game_rules = " 1. Select one of 6 categories.\
    2. The game will randomly generate a word from your choosen category.\
    3. Enter one letter at a time to try to guess this word.\
    4. You have 4 attempts."\

print(game_rules)

print("Please see list of word categories below:")

# All category headings appear in row 1 of spreadsheet
wks = SHEET.worksheet("wordlist")
words = wks.row_values(1)

# Use list comprehension to convert list of lists from google sheet into list of strings"""
word_categories = [''.join(ele) for ele in words]

print(word_categories)


""" Player selects one of 6 word categories from list of strings pulled from
Wordle-Hangman google sheet """
choice = 0
def pick_category_word():
# while choice <= 6:
    choice = int(input("Enter your choice = "))
    if choice > 6:
        print("This is not a valid category number")
        choice = int(input("Enter your choice = "))
    category = word_categories[choice - 1]
    picked = SHEET.worksheet("wordlist").find(category).value
    print("Your choice is: ",(picked))
    word_list = wks.col_values(choice)
    # print(word_list[1:])
    random_word = random.choice(word_list[1:])
    print('The word has' , len(random_word), 'letters')
    return random_word

pick_category_word()

def update():
    correct = ['_'] * len(random_word)
    incorrect = []
    for x in correct:
        print(x, end=' ')
    print()

def wait():
    for i in range(5):
        print('.', end ="")
        sleep(.5)
    print()
print("Let me check")

wait()

update(random_word)
bodyParts(len(incorrect))

# To Do - function asking player if they wish to play a new game or exit game.

def new_game_exit():

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
                print("You lose")
                print("The word was" , random_word)
                break
        if '_' not in correct:
            print("You win")
            break