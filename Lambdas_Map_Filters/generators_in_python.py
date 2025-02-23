#Generator functions like functions but instead of returning a value and exiting, it pauses the function and saves the state of the function.
#generator similar to list but they are not stored in memory
#generator is an iterator and dont indexing

#In order to create generetor you need to create a function and use yield instead of return (generator function)

def genarator_function():
    counter = 0
    while counter < 10:
        yield counter   #It gives generator object
        counter += 1

print(list(genarator_function()))