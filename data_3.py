word = input("Enter a word: ")

first_letter = word[0]
resultString = first_letter

for i in range(1, len(word)):
    if word[i] == first_letter:
        char = '$'
    else:
        char = word[i]
    resultString += char

print(resultString)
