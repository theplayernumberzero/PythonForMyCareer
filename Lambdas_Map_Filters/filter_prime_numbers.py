def isItPrime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, n):
            if n%i == 0:
                return False
        return True

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers)

prime_numbers = list(filter(isItPrime, numbers))
print(prime_numbers)