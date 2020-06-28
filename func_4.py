def reverse_string(input_string):
    new_string = ""
    for i in range(len(input_string)-1, -1, -1):
        new_string += input_string[i]
    return new_string


print(reverse_string("1234abcd"))
