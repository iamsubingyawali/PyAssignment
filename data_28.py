def add_dict_key(dict_input):
    key = len(dict_input)
    dict_input[key] = (key + 1) * 10
    return dict_input


input_dict = {0: 10, 1: 20}

print(add_dict_key(input_dict))
