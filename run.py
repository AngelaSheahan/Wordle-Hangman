# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
import random
from hangman_parts import parts
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

words = SHEET.worksheet("wordlist").get_all_values()

""" Use list comprehension to convert list of lists from google sheet
into list of strings"""
words_string = [''.join(ele) for ele in words]

# Use random() to generate a random word from list of words
picked = random.choice(words_string)

print('The word has', len(picked), 'letters')

correct_guesses = ['_'] * len(picked)

print(correct_guesses)

wrong_guesses = [ ]

# guess = input("Enter a letter: ")

def data_validation(guess):
    guess = input("Enter a letter: ")
    for x in guess:
        if guess.isdigit():
            print("enter a letter not a number")
        elif len(guess) > 1:
            print("enter only 1 letter")
        elif guess == 0:
            print(" enter a letter")
        else:
            return guess

data_validation(guess)

def update():
    for i in right:
        print(i,  end=' ')
    print()
print('Let me think of a word')

def wait():
    for i in range(5):
        print('.', end = '')
        sleep(.5)
    print()

wait()

update()
parts(len(wrong))

while True:

    print('==========================================')

    guess = input('Guess a letter: ')
    print('Let me check')
    wait()

    
    if guess in picked:
        index = 0
        for i in picked:
            if i == guess:
                right[index] = guess
            index +=1
        update()

    else:
        if guess not in wrong:
            wrong.append(guess)
            parts(len(wrong))
            
        else:
            print('You already picked that')
        print(wrong)
    if len(wrong) > 4:
        print('You loose')
        print('The word is:' , picked)
        break

    if len(wrong) > 4:
        print('You loose')
        print('The word is: ', picked)
        break

    if '_' not in right:
        print('You win')
        break






# words = SHEET.worksheet('wordlist')
# data = words.get_all_values()
# print(data)

# The secret word the player is trying to guess
# secretWord = "cacao"
# lettersGuessed = ""
# failureCount = 5

# while failureCount > 0:
#     # Get the guessed letter from the player
#     guess = input("Enter a letter: ")

#     if guess in secretWord:
#         # Player guessed a correct letter!
#         print(f"There is one or more {guess} in the secret word.")
#     else:
#         failureCount -= 1
#         print(f"Incorrect. There are no {guess} in the secret word. You have {failureCount} attempts left")

#     lettersGuessed = lettersGuessed + guess
#     wrongLetterCount = 0

#     for letter in secretWord:
#         if letter in lettersGuessed:
#             print(f"{letter}", end="")
#         else:
#             print(f"_", end="")

#             wrongLetterCount += 1
#     print("")

# # no wrong letters, then the player won
#     if wrongLetterCount == 0:
#         print(f"Congratulations! The secret word was {secretWord}. You won!")
#         break

# else:
#     print("Sorry you didn't win this time. Try again")


        




