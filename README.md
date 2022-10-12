# WORDLE HANGMAN
-------
Wordle hangman is based on the traditional pen and paper game. You can read more about it on [Wikipedia](https://en.wikipedia.org/wiki/Hangman_(game)).  I have also encorporated the concept of the hugely popular 5 letter word guess game, Wordle. Hence, every word that the player has to guess is 5 letters in length.<br/><br/>
The player enters their name. The player is then presented with a list of 6 word categories to choose from.<br/>The player chooses which category they wish to guess a word from.<br/>The word categories and their corresponding words are found in a google sheet (Wordle-Hangman).<br/>A word is picked by random from the players choosen category; this word is hidden from the player.<br/>
The player has 5 attempts to guess the word; one letter at a time.<br/> Like the traditional hangman game, each time the player guesses an incorrect letter an item is added to the graphical representation of the hanging gallows:
- 1 incorrect word - head.
- 2nd incorrect word - body.
- 3rd incorrect word - both arms.
- 4th incorrect word - both legs.


# Features
____
## Existing Features
- Category Selection<br/>
    - A player can choose the category of interest (from which the word to be guessed is sourced) by entering the associated number of that category e.g. 1. Countries. . These categories are presented to the player in the form of a list on the terminal. The categories are pulled from a google sheet.<br/> <br/>
    ![category list](views/screenshots/category_list.jpg)<br/>
    
- Random Word generation
    - A word is randomly 'pulled' from the player selected category from the google sheet(Wordle-Hangman) and presented to the player as a series of five underscores. This is the word the player has to guess.
- Game accepts player input, one letter at a time.<br/> <br/>
![player guess](views/screenshots/correct%20guesses.jpg)<br/>
- Data validation on player category choice and on player guesses . 
    - Player cannot enter a category number < 1 or >=7, as these are not valid category numbers. There are presently word for only 6 categories in my google sheet. In addition a player cannot enter a letter in error instead of a number.<br/><br/>
    ![category number error](views/screenshots/cat_number.jpg) <br/>
    ![category letter error](views/screenshots/cat_letter.jpg) <br/><br/>
    - Player cannot enter a number instead of a letter for their guess.<br/> <br/>
    ![guess number error](views/screenshots/guess_number.jpg)
    >
    - Player may enter a number of letters in each guess experience, but only the first letter of the string entered is accepted as the valid guess letter for that guess.<br/>
    ![multi-letters entered in one guess](views/screenshots/more_than_one_letter.jpg) <br/>
    - Player will be allerted if they have entered an incorrect letter already entered in a previous guess. <br/> 
    ![letter already guessed](views/screenshots/already_guessed.jpg)<br/>
 
- Guess Tracking in the form of a list of incorrect guesses displayed on screen and the 
correct words entered into the appropriate underscore.<br/>
![all guesses tracked & displayed on screen](views/screenshots/guess_tracking.jpg)<br/>
- Graphical representation of gallows with elements added each time player guesses an incorrect word. (stored in the hangman_parts.py)<br/>
![1 incorrect guess](views/screenshots/1_incorrect_guess.jpg)<br/>
![2 incorrect guesses](views/screenshots/2_incorrect_guesses.jpg)<br/>
![3 incorrect guesses](views/screenshots/3_incorrect_guesses.jpg)<br/>
![4 incorrect guesses](views/screenshots/4_incorrect%20guesses.jpg)<br><br/>
- Data maintained in class instances (There are 2 classes in my code; class Hangman in hangman.py and class Dictionary in dictionary.py)
- A play again Y/N feature.<br/>
![play again feature](views/screenshots/win.jpg)<br/>
- Once the Players name is captured, it is followed through the game to personalise the gaming experience (see image above). In addition, if the player chooses to play another game, their name is carried through also; hence they do not have to re-enter their name.

# Future Features

# Data Model

# Testing

Manual:
- PEP8
- incorrect inputs
- local terminal & Heroku terminal

# Bugs
## Solved
- indexing in list of categories
int(input) accepted letters - see base 10 error

# Remaining Bugs

# Validator Testing

# Deployment
### The project was deploying using Code Institutes mock terminal for Heroku.
- The steps for deployment:
    

# Credits
https://www.geeksforgeeks.org/python-convert-list-of-lists-to-list-of-strings/

hangman videos that helped me along

1. https://www.youtube.com/watch?v=Ff--def_1q0
2. https://www.youtube.com/watch?v=7sVnul-StrU

data validation:

https://www.educba.com/python-validation/





    
        

