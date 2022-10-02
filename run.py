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

game_intro = "Welcome to Wordle-Hangman! As the name implies, all words are of 5\
    letters in length. You, the player, selects a Word Category. The game then\
    randomly selects a word from this category for you to guess. Good Luck!" 

print(game_intro)  

game_rules = " 1. Select one of 6 categories.\
    2. The game will randomly generate a word from your choosen category.\
    3. Enter one letter at a time to try to guess this word.\
    4. You have 4 attempts."

print(game_rules)

# All category headings appear in row 1 of spreadsheet
words = SHEET.worksheet("wordlist").row_values(1)

# Use list comprehension to convert list of lists from google sheet into list of strings"""
words_string = [''.join(ele) for ele in words]

choice = input ("please select a category from the following list, " {words_string}. "Enter you choice here": )


# Use random() to generate a random word from the choosen category of words.
picked = random.choice(SHEET.worksheet.col_values.choice)

print(picked)

print('The word has' , len(picked), 'letters')

correct = ['_'] * len(picked)
incorrect = []

def update():
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

update()
bodyParts(len(incorrect))

# function asking player if they wish to play a new game or exit game
def new_game_exit():
    

    

while True:

    print('############################################')
    guess = input("Guess one letter: ")[0]

    if guess.isnumeric():
        print("Enter a letter not a number: ")
        continue
    if guess in picked:
        index = 0
        for x in picked:
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
            print("The word was" , picked)
            break
    if '_' not in correct:
        print("You win")
        break







        




