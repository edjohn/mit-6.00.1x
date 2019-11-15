bob_count = 0
letter_index = 0
for letter in s:
    if s[letter_index:letter_index+3] == 'bob':
        bob_count += 1
    letter_index += 1
print("Number of times bob occurs is: " + str(bob_count))