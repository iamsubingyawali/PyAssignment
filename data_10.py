def remove_odd(string):
    char_list = list(string)
    removed_list = list()
    for i in range(len(char_list)):
        if i % 2 == 0:
            removed_list.append(char_list[i])
    return "".join(removed_list)


word = input("Enter a word: ")
print(remove_odd(word))
