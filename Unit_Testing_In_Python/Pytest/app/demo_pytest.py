def add(a,b):
    return a+b

def mul(a,b):
    return a*b

def div(a,b):
    if b == 0:
        raise ValueError("Cant divided by 0")
    return a/b

def discount_season():
    return True