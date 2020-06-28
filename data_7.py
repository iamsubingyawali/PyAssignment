def return_largest(list_input):
    largest = list_input[0]

    for item in list_input:
        if len(item) > len(largest):
            largest = item
    return len(largest)
