word = input("Enter a word: ")
vowel_count = 0

for i in range(len(word)):
    if word[i].lower() in 'aeiou':
        vowel_count += 1

print("Number of vowels:", vowel_count)
