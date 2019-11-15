def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:
    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    totalScore = 0
    # Keep track of the total score
    while calculateHandlen(hand) > 0:
    # As long as there are still letters left in the hand:
        print('Current Hand: ', end = ' ')
        displayHand(hand)
        # Display the hand
        word = input('Enter word, or a "." to indicate that you are finished: ')
        # Ask user for input
        if word == '.':
        # If the input is a single period:
            break
            # End the game (break out of the loop)
        else:
        # Otherwise (the input is not a single period):
            if isValidWord(word, hand, wordList) == False:
            # If the word is not valid:
                print('Invalid word, please try again.')
                print('')
                # Reject invalid word (print a message followed by a blank line)
            else:
            # Otherwise (the word is valid):
                totalScore += getWordScore(word, n)
                print('"' + word + '"' + ' earned ' + str(getWordScore(word, n)) + ' points. ' + 'Total: ' + str(totalScore) + ' points')
                print('')
                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                hand = updateHand(hand, word)
                # Update the hand 
    if calculateHandlen(hand) == 0:
        print('Run out of letters. Total score: ' + str(totalScore) + ' points.')        
    else:
        print('Goodbye! Total score: ' + str(totalScore) + ' points.')        
    # Game is over (user entered a '.' or ran out of letters), so tell user the total score