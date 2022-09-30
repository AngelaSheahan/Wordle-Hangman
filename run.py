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

words = SHEET.worksheet("wordlist").get_all_values()

""" Use list comprehension to convert list of lists from google sheet
into list of strings"""
words_string = [''.join(ele) for ele in words]

# Use random() to generate a random word from list of words
picked = random.choice(words_string)

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




# Print to terminal the length of the word pulled from my google sheet
# print('The word has', len(picked), 'letters')

# correct_guesses = ['_'] * len(picked)

# print(correct_guesses)

# wrong_guesses = [ ]

# guess = input("Enter a letter: ")

# def input_validation(guess):
#         if guess.isdigit():
#             print("enter a letter not a number")
#         elif len(guess) > 1:
#             print("enter only 1 letter")
#         elif len(guess) == "":
#             print(" enter a letter")
#         else:
#             return guess

# input_validation(guess)
            

# def update():
#     for i in correct_guesses:
#         print(i,  end=' ')
#     print()
# print('Let me think of a word')

# def wait():
#     for i in range(5):
#         print('.', end = '')
#         sleep(.5)
#     print()

# wait()

# update()

# parts(len(wrong_guesses))

# while True:

#     print('==========================================')

#     wait()
  
#     if guess in picked:
#         index = 0
#         for i in picked:
#             if i == guess:
#                 correct_guesses[index] = guess
#             index +=1
#         update()

#     else:
#         if guess not in wrong_guesses:
#             wrong_guesses.append(guess)
#             parts(len(wrong_guesses))
            
#         else:
#             print('You already picked that')
#         print(wrong_guesses)

#     if len(wrong_guesses) > 4:
#         print('You loose')
#         print('The word is: ', picked)
#         break

#     if '_' not in correct_guesses:
#         print('You win')
#         break






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


        




