def first_two_strings(string):
    if len(string) < 2:
        return "Empty String"
    else:
        result_string = string[0] + string[1] + string[-2] + string[-1]
        return result_string


word = input("Enter a word: ")

print(first_two_strings(word))
