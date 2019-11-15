current_sentence = s[0]
longest_sentence = s[0]
length_longest_sentence = 0
for letter in range(len(s) - 1):
    if s[letter] <= s[letter+1]:
        current_sentence += s[letter+1]
        if len(current_sentence) > length_longest_sentence:
            length_longest_sentence = len(current_sentence)
            longest_sentence = current_sentence
    else:
        current_sentence=s[letter+1]
    letter += 1            
print("Longest substring in alphabetical order is: " + longest_sentence)
