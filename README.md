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
    - A player can choose the category of interest (from which the word to be guessed is sourced) by entering the associated number of that category e.g. 1. Countries. . These categories are presented to the player in the form of a list on the terminal. The categories are pulled from a google sheet.<br/>
    
- Random Word generation
    - A word is randomly 'pulled' from the player selected category from the google sheet(Wordle-Hangman) and presented to the player as a series of five underscores. This is the word the player has to guess.
- Accepts player input, one letter at a time. 
- Data validation on player category choice and on player guesses . 
    - Player cannot enter a category number < 1 or >=7, as these are not valid category numbers. There are presently word for only 6 categories in my google sheet. 
    - Player cannot enter a number instead of a letter for their guess.
    - Player may enter a number of letters in each guess experience, but only the first letter of the string entered is accepted as the valid guess letter for that guess.
    - Player will be allerted if they enter a letter already entered in a previous guess.  
 
- Guess Tracking in the form of a list of guesses is displayed on screen.
- Player guess tracking.
- Graphical representation of gallows with elements added each time player guesses an incorrect word. (stored in the hangman_parts.py)
- Data maintained in class instances (There are 2 classes in my code; class Hangman in hangman.py and class Dictionary in dictionary.py)
- A player again Y/N feature.
- Player name is followed through the game to personalise the game experience.


    
        

