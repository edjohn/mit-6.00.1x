def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    tempHand = []
    for key in hand.keys():
        for item in range(hand[key]):
            tempHand.append(key)
    if word in wordList:
        for letter in word:
            if letter not in tempHand:
                return False
            else:
                tempHand.remove(letter)
        return True
    else:
        return False