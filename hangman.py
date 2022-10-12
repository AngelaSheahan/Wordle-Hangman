from hangman_parts import bodyParts
from time import sleep


class Hangman:


    # Update correct list with correct answers
    def __update(self):
        """
        Add correct guesses to the correct list. The end=' ' is added here to ensure that each
        correct letter is added beside each other in list, not on separate lines.
        """
        for x in self.correct:
            print(x, end=' ')
        print()


    def __wait(self):
        """
        Python time sleep() function suspends execution for 5 seconds. This I use to
        build up suspension in the game after a player makes a guess. There is a 5 second
        delay before the result (i.e. is the players guess correct or incorrect?) is displayed.
        """

        for i in range(5):
            print('.', end=" ")
            sleep(.5)
        print()


    def information(self):
        """
        This game is called, Wordle-Hangman, combining the New\n
        York Times hugely successful, daily 5 letter guessing\n
        game, Wordle, and the traditional game, Hangman.\n
        When this function is called, it displays a game \n
        introduction and the game rules to the screen
        """
        game_intro = "Welcome to WORDLE HANGMAN! This is a 5 letter guessing game.\nGOOD LUCK!"
        game_rules = "1. Select one of 6 categories.\n2. The game will randomly generate a word from your choosen category.\n3. Enter one letter at a time to try to guess this word.\n4. You have 4 attempts.\n"
        print("-------------------------------------------------------")
        print(game_intro)
        print(game_rules)
        print("-------------------------------------------------------")


    def play_game(self, random_word, player_name):
        """
        Run a while loop to collect an input(a guess) from the user via the\n 
        terminal. All correct letter guesses will fill the correct\n
        letter underscore slot in the 'correct' list; incorrect\n
        letter guesses are be added to the 'incorrect' list and\n 
        also displayed on screen. When the player makes incorrect\n 
        guesses, the bodyParts function is called (which is stored\n
        in the hangman_parts.py). The loop will repeatedly request \n
        data, until all the underscores are replaced by words (i.e.)\n
        all the correct letters have been guessed), or the incorrect\n
        list is > 4. Run a second While loop in the event that the\n
        player wishes to play again. The initialise_game() function\n
        is called to clear the variable contents.
        """
        self.correct = ['_'] * len(random_word)
        incorrect = []

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
                        self.correct[index] = guess
                    index += 1
                self.__update()

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
            if '_' not in self.correct:
                print(f"You win {player_name}")
                break
            