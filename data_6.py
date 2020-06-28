def modify_string(list_sentence, not_index, poor_index):
    if not_index is None or poor_index is None:
        return " ".join(list_sentence)
    else:
        for i in range(poor_index - not_index+1):
            list_sentence.pop(not_index)

        list_sentence.insert(not_index, "good")
        return " ".join(list_sentence)


# Finding the index of 'not' and 'poor'
def find_index(sentence):
    list_sentence = sentence.split()
    try:
        not_index = list_sentence.index('not')
    except ValueError:
        not_index = None

    try:
        poor_index = list_sentence.index('poor', not_index)
    except ValueError:
        poor_index = None

    return modify_string(list_sentence, not_index, poor_index)


input_sentence = "The lyrics is not that poor !"
print("Input: ", input_sentence)
print("Output: ", find_index(input_sentence))
