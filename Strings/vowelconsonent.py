x = input("Enter a string: ")
vowels = 0
consonants = 0
for ch in x:
    if ch.isalpha():
        if ch in "aeiouAEIOU":
            vowels += 1
        else:
            consonants += 1
print("Vowels:", vowels)
print("Consonants:", consonants)
