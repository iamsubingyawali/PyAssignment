def remove_key(dict_input, key_to_remove):
    try:
        del dict_input[key_to_remove]
        return dict_input
    except KeyError:
        return "Key Doesn't exist."


input_dict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print(remove_key(input_dict, 3))
