def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    availableLetterList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    availableLetterString = ''
    # FILL IN YOUR CODE HERE...
    for letter in lettersGuessed:
        if letter in availableLetterList:
            availableLetterList.remove(letter)
    for letter in availableLetterList:
        availableLetterString += letter
    return availableLetterString