import gspread
import random
from google.oauth2.service_account import Credentials


class Dictionary:

    def __init__(self):
        SCOPE = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive.file",
            "https://www.googleapis.com/auth/drive"
        ]
        CREDS = Credentials.from_service_account_file('creds.json')
        SCOPED_CREDS = CREDS.with_scopes(SCOPE)
        GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
        SHEET = GSPREAD_CLIENT.open('Wordle-Hangman')
        self.wks = SHEET.worksheet("wordlist")
        self.word_categories = []
        self.choice = 0
        self.__load_categories()

    def __load_categories(self):
        """
        The player selects one of 6 word categories from the list of strings (stored in 
        the variable, words) pulled from Wordle-Hangman google sheet. This list consists 
        of the values in row 1 (i.e. the column headings). The Function load_categories 
        pulls the list of categories from the spreadsheet, wordlist. This spreadsheet values
        are assigned to the global variable, wks.
        """
        # All category headings appear in row 1 of spreadsheet
        words = self.wks.row_values(1)
        # Use list comprehension to convert list of lists from google sheet into list of strings"""
        self.word_categories = [''.join(ele) for ele in words]


    def __choose_category(self):
        """
        The list of categories is printed to the screen. The player enters their category 
        choice (from 1 to 6). This category choice is stored in the variable picked. Data 
        Validation prevents the player from entering a category below 1 or above 6 or from
        entering a letter instead of a number.
        """
        print("Please see list of word categories below:")
        print(self.word_categories)
        while True:
            try:
                self.choice = int(input("Enter your choice = \n"))
            except ValueError:
                print("This is not a valid number. Please try again")
                continue
            if (self.choice < 1) or (self.choice >= 7):
                print("This is not a valid category number. Please try again")
            else:
                break

        category = self.word_categories[self.choice - 1]
        picked = self.wks.find(category).value
        print("Your choice is: ", (picked))


    def select_random_word(self):
        """ 
        The computer randomly selects a word from the category selected by the player.
        This word is stored in the variable, random_word. The word is not displayed to 
        the screen but is represented on the screen in the form of 5 underscores.
        """

        self.__choose_category()

        word_list = self.wks.col_values(self.choice)
        random_word = random.choice(word_list[1:])
        print('The word has', len(random_word), 'letters')
        return random_word
