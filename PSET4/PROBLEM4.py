def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    tempLength = 0
    for value in hand.values():
        tempLength += value
    return tempLength