def check_prime(num):
    if num < 1:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
                break
        return True


number = int(input("Enter a number: "))
print(check_prime(number))
