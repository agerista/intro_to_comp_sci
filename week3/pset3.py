from string import ascii_lowercase

# Problem 1


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    seen = []

    for char in lettersGuessed:
        if char in secretWord:
            seen.append(char)
    return sorted(seen) == sorted(secretWord)


# Problem 2


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guess = ""

    for char in secretWord:
        if char not in lettersGuessed:
            guess += "_ "
        else:
            guess += char

    return guess


# Problem 3


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    avail = ascii_lowercase

    for char in lettersGuessed:
        avail = avail.replace(char, '')
    return avail


# Problem 4


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    guesses = 8
    guessed = False
    lettersGuessed = []

    print ("Welcome to the game, Hangman!\nI am thinking of a word that is " + str(len(secretWord)) + " letters long.")

    while not guessed and guesses > 0:

        print ("-------------")
        print ("You have " + str(guesses) + " guesses left.")

        print ("Available letters: " + getAvailableLetters(lettersGuessed))
        guess = (input("Please guess a letter: ")).lower()

        if guess in lettersGuessed:
            print ("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
            continue
        lettersGuessed.append(guess)
        tried = getGuessedWord(secretWord, lettersGuessed)

        if guess in tried:
            print ("Good guess: " + tried)

        else:
            print ("Oops! That letter is not in my word: " + tried)
            guesses -= 1

        match = isWordGuessed(secretWord, lettersGuessed)
        if match:
            guessed = True

    print ("-------------")
    if match:
        print ("Congratulations, you won!")

    else:
        print ("Sorry, you ran out of guesses. The word was {}").format(secretWord)
