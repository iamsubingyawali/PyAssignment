def count_char(string):
    count_dict = {}
    for item in string:
        occ = string.count(item)
        count_dict[item] = occ
    return count_dict


word = input("Enter a word: ")
print(count_char(word))
