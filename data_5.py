def modify_string(word):
    if len(word) < 3:
        return word
    else:
        if word[-3:len(word)] == "ing":
            return word + "ly"
        else:
            return word + "ing"


input_word = input("Enter a word: ")
print(modify_string(input_word))
