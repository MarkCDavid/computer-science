# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
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
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    return all([letter in letters_guessed for letter in secret_word])



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    return ''.join([letter if letter in letters_guessed else '_ ' for letter in secret_word])



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    return ''.join([letter if letter not in letters_guessed else '' for letter in string.ascii_lowercase])
    
WARNINGS = "warnings"
GUESSES = "guesses"
GUESSED_LETTERS = "guessed_letters"

def get_default_game_state():
    return { WARNINGS: 3, GUESSES: 6, GUESSED_LETTERS: [] }

def warn_user(game_state, message):
    if game_state[WARNINGS] > 0:
        game_state[WARNINGS] -= 1
        print(f"{message} {game_state[WARNINGS]} warnings left.")
        return True
    else:
        game_state[GUESSES] -= 1
        return False

def get_user_guess(game_state, additional_valid_symbols=None):
    print(f"You have {game_state[GUESSES]} guesses.")
    print(f"You can guess { get_available_letters(game_state[GUESSED_LETTERS])}.")

    user_guess = input("Guess: ").lower()

    if additional_valid_symbols is not None and user_guess in additional_valid_symbols:
        return (user_guess, True)

    if len(user_guess) != 1 or not str.isalpha(user_guess):
        return (None, warn_user(game_state, "Invalid input!"))
       
    if user_guess in game_state[GUESSED_LETTERS]:
        return (None, warn_user(game_state, f"You have already guessed {user_guess}!"))

    return (user_guess, True)

def check_loss(game_state, secret_word):
    if game_state[GUESSES] <= 0:
        print("You ran out of guesses!")
        print(f"The word was {secret_word}.")
        return True
    return False

def check_victory(game_state, secret_word):
    if is_word_guessed(secret_word, game_state[GUESSED_LETTERS]):
        print("Congratulations! You guessed the word!")
        print(f"Score: {game_state[GUESSES] * len(set(secret_word))}")
        return True
    return False

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    
    game_state = get_default_game_state()

    print(f"You are guessing a word with {len(secret_word)} letters.")

    while True:
        print("##################")
        print(get_guessed_word(secret_word, game_state[GUESSED_LETTERS]))

        if check_victory(game_state, secret_word): break        
        if check_loss(game_state, secret_word): break

        (user_guess, keep_guessing) = (None, True)
        while user_guess is None and keep_guessing is True:
            (user_guess, keep_guessing) = get_user_guess(game_state)

        game_state[GUESSED_LETTERS].append(user_guess)
        
        if user_guess not in secret_word:
            game_state[GUESSES] -= 2 if user_guess in 'aeiou' else 1
            

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word = my_word.replace(' ', '')
    if len(my_word) != len(other_word):
      return False

    return all([True if pair[0] == '_' or pair[0] == pair[1] else False for pair in zip(my_word, other_word)])



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    matched_words = list(filter(lambda word: match_with_gaps(my_word, word), wordlist))
    if len(matched_words) == 0:
      print('No matches found!')
    else:
      print(' '.join(matched_words))

LIST_ALL = '*'

def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
        
    game_state = get_default_game_state()

    print(f"You are guessing a word with {len(secret_word)} letters.")

    while True:
        print("##################")
        print(get_guessed_word(secret_word, game_state[GUESSED_LETTERS]))

        if check_victory(game_state, secret_word): break        
        if check_loss(game_state, secret_word): break

        (user_guess, keep_guessing) = (None, True)
        while user_guess is None and keep_guessing is True:
            (user_guess, keep_guessing) = get_user_guess(game_state, [LIST_ALL])

        if user_guess == LIST_ALL:
          show_possible_matches(get_guessed_word(secret_word, game_state[GUESSED_LETTERS]))
          continue

        game_state[GUESSED_LETTERS].append(user_guess)
        
        if user_guess not in secret_word:
            game_state[GUESSES] -= 2 if user_guess in 'aeiou' else 1

# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
