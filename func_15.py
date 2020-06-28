def filter_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


filtered_elements = filter(filter_even, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(list(filtered_elements))
