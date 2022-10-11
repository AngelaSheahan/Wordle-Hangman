from dictionary import Dictionary
from hangman import Hangman


def main():
    myDictionary = Dictionary()
    myDictionary.load()

    myHangman = Hangman()
    myHangman.information()

    player_name = input("Please enter your name:  \n")
    print("Welcome " + player_name)
    print("-----------------------------------------------------------------")

    while True:
        random_word = myDictionary.select_random_word()
        myHangman.play_game(random_word, player_name)
        replay = (input(f"Do you want to play again {player_name}? [y] / [n]: \n"))
        if replay == 'n':
            print(f"Goodbye {player_name}!")
            break


main()

