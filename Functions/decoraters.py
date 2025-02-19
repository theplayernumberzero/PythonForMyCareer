def chocolate():
    print("chocolate")

def decarator(func):    #modify existing function
    def wrapper():
        print("Wrapper upside")
        func()
        print("Wrapper downside")
    return wrapper

chocolate = decarator(chocolate)    #only pass func name
chocolate()

#Second way
def decarator2(func):    
    def wrapper():
        print("Wrapper upside")
        func()
        print("Wrapper downside")
    return wrapper

@decarator2
def strawberry():
    print("strawberry")

strawberry()

#decoration with paramters

def decarator3(func):    
    def wrapper(*args, **kwargs):   #flexible
        print("Wrapper upside")
        func(*args, **kwargs)
        print("Wrapper downside")
    return wrapper

@decarator3
def strawberry():
    print("strawberry")

@decarator3
def myName(name):
    print(f"my name is {name}")

strawberry()
myName("Bahadir")

#decoration with return values
def discount_decerator(func):
    def wrapper(price):
        func(price) #first call then return as you manipulate
        return func(price) / 2
    return wrapper

@discount_decerator
def total(price):
    return price

number = total(100)
print(number)
