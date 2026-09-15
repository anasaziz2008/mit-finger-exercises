# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()

def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True


def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    progress = ""
    for letters in secret_word:
        if letters in letters_guessed:
            progress += letters
        else:
            progress += "*"
    return progress


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    available_letters = ""
    for letters in string.ascii_lowercase:
        if letters not in letters_guessed:
            available_letters += letters
    return available_letters


def hangman(secret_word, with_help):
    """
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a single letter (or help character '!'
      for with_help functionality)

    * If the user inputs an incorrect consonant, then the user loses ONE guess,
      while if the user inputs an incorrect vowel (a, e, i, o, u),
      then the user loses TWO guesses.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    -----------------------------------
    with_help functionality
    -----------------------------------
    * If the guess is the symbol !, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    word_length = len(secret_word)
    guesses_remaining = 10
    letters_guessed = []
    
    print("Welcome to Hangman!")
    print(f"I am thinking of a word that is {word_length} letters long.")
    
    while not has_player_won(secret_word, letters_guessed) and guesses_remaining > 0:
        print("------")
        print(f"You have {guesses_remaining} guesses left.")
        print(f"Available letters: {get_available_letters(letters_guessed)}")
        
        user_guess = input("Please guess a letter: ").lower()
        if user_guess not in "!" and (user_guess not in string.ascii_lowercase):
            print("only alphabets are allowed")
            continue
        
        if with_help and user_guess == "!":
            if guesses_remaining < 3:
                print("You do not have enough guesses remaining to use the help feature.")
            else:
                missing_letters = []
                for letter in secret_word:
                    if letter not in letters_guessed:
                        missing_letters.append(letter)
                if missing_letters:
                    revealed_letter = random.choice(missing_letters)
                    letters_guessed.append(revealed_letter)
                    guesses_remaining -= 3
                    print(f"Letter revealed: {revealed_letter}")
                    print(get_word_progress(secret_word, letters_guessed))
        else:
            if user_guess in letters_guessed:
                print("Oops! You've already guessed that letter:", get_word_progress(secret_word, letters_guessed))
            elif user_guess in secret_word:
                letters_guessed.append(user_guess)
                print("Good guess:", get_word_progress(secret_word, letters_guessed))
            else:
                letters_guessed.append(user_guess)
                print("Oops! That letter is not in my word:", get_word_progress(secret_word, letters_guessed))
                if user_guess in "aeiou":
                    guesses_remaining -= 2
                else:
                    guesses_remaining -= 1

    print("------")
    if has_player_won(secret_word, letters_guessed):
        unique_letters = len(set(secret_word))
        score = (guesses_remaining + (4 * unique_letters)) + (3 * len(secret_word))
        print("Congratulations, you won!")
        print(f"Your total score for this game is: {score}")
    else:
        print(f"Sorry, you ran out of guesses. The word was {secret_word}")    
    
# hangman("wildcard", True)  # Example call to the hangman function

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

if __name__ == "__main__":
    # To test your game, uncomment the following three lines.

    # secret_word = choose_word(wordlist)
    # with_help = False
    # hangman(secret_word, with_help)

    # After you complete with_help functionality, change with_help to True
    # and try entering "!" as a guess!

    ###############

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your pset. However, please run ps2_student_tester.py
    # one more time before submitting to make sure all the tests pass.
    pass
