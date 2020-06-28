def remove_index(string, index):
    word_list = list(string)
    word_list.pop(int(index))
    result_word = "".join(word_list)
    return result_word


word = input("Enter the String: ")
index_remove = input("Enter the index to remove: ")
print(remove_index(word, index_remove))

