#recursion: When you use function in function itself

def factorial(number):
    if number == 1:
        return 1
    else:
        return number * factorial(number - 1)
    
factorial = factorial(5)
print(f"5! = {factorial}")