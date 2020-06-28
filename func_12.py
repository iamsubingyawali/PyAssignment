from random import randrange


def random_multiply(number):
    return number * randrange(100)


num = int(input("Enter a number: "))
print(random_multiply(num))
