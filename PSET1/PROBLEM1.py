vowel_count = 0
for vowel in s:
    if (vowel == 'a' or vowel == 'e' or vowel == 'i' or vowel == 'o' or vowel == 'u'):
        vowel_count += 1
print("Number of vowels: " + str(vowel_count))