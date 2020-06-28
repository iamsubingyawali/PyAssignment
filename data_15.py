def insert_into_middle(string, word):
    string_len = int(len(string))
    if string_len % 2 != 0:
        return "Can't Insert"
    else:
        middle = int(string_len / 2)
        added_string = string[:middle] + word + string[middle:]
        return added_string


string_input = input("Enter a String to place on both sides: ")
word_input = input("Enter a word to insert into the middle: ")
print(insert_into_middle(string_input, word_input))
