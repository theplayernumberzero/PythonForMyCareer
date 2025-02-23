#lambdas are functions without a name (anonymous functions), it is one line function

def square(num):
    return num**2

print(square(5))

#lambda function 

result = (lambda num: num**2)(5)    #you can use default parameter as well
print(result)
