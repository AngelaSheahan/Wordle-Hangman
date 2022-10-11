from hangman_parts import bodyParts


class Hangman:

    def __init__(self):
        self.random_word
        self.correct = []
        self.incorrect = []
        self.guess = []
        self.__play_game()
        self.random_word = []

    def __play_game(self):
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
        self.guess = input("Guess one letter: \n")[0]

        if self.guess.isnumeric():
            print("Enter a letter not a number: ")
            continue

        if self.guess in self.random_word:
            index = 0
            for x in self.random_word:
                if x == self.guess:
                    self.correct[index] = self.guess
                index += 1
            self.__update()

        else:
            if self.guess not in self.incorrect:
                self.incorrect.append(self.guess)
                self.bodyParts(len(self.incorrect))
            else:
                print("You have already guessed that")
            print(self.incorrect)
            if len(self.incorrect) > 4:
                print(f"You lose {player_name}!")
                print("The word was", self.random_word)
                break
        if '_' not in self.correct:
            print(f"You win {player_name}")
            break
