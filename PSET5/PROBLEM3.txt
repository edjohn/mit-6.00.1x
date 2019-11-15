class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        bestShift = 0
        shift = 0
        highestWordCount = 0
        
        while shift < 27:
            validWordCount = 0
            for word in self.message_text.split(' '):
                if is_word(self.get_valid_words(), Message(word).apply_shift(shift)):
                    validWordCount += 1
            if validWordCount > highestWordCount:
                bestShift = shift
                highestWordCount = validWordCount
            shift += 1
        return bestShift, self.apply_shift(bestShift)