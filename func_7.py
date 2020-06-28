def check_upper(test_string):
    count = 0
    for letter in test_string:
        if letter.isupper():
            count += 1
    return count


def check_lower(test_string):
    count = 0
    for letter in test_string:
        if letter.islower():
            count += 1
    return count


input_string = input("Enter a string: ")
print("Number of Uppercase Letters:", check_upper(input_string))
print("Number of Lowercase Letters:", check_lower(input_string))