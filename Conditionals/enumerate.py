#enumerate() is a built-in function that allows you to loop over an
#iterable (like a list, tuple, or string) 
#while also keeping track of the index (or position) of the current item

#without enumerate
fruits = ['apple', 'banana', 'cherry']
index = 0
for fruit in fruits:
    print(index, fruit)
    index += 1

#with enumerate
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(index, fruit)