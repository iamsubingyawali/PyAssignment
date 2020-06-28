def exchange(word):
    word_list = list(word)
    word_list[0], word_list[-1] = word_list[-1], word_list[0]
    result_word = "".join(word_list)
    return result_word


input_word = input("Enter a word: ")
print(exchange(input_word))