def speed(distance, time):
    print(distance/time)

def area(radius, pi=3.14):  #default value
    print(pi*radius*radius)

def calculatedArea(radius, pi=3.14):  #default value
    return pi*radius*radius

#returning multiple value
def circle(r):
    area = 3 * r * r
    circumference = 2 * 3 * r
    return area, circumference

def add(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

def remove_duplicates(numbers):
    new_list=[]
    for number in numbers:
        if number not in new_list:
            new_list.append(number)
    return new_list
    #return list(set(numbers))    or you can directly use that

def increment():
    global count
    count = count + 1
    print(count)

#take as much as user wnat parameter
def addWithUnlimitedParameter(*args): #args hold in function as a tuple
    sum = 0
    for n in args:
        sum = sum + n
    print(sum)


speed(distance=100, time=2)
speed(time=2, distance=100)

area(10)
area(10, 3) #you can edit default value or not

myArea = calculatedArea(10)
print(myArea)

area, circumference = circle(10)
print(area, circumference)

numbers = [1,2,3,4,5]
sum = add(numbers)
print(sum)

numbers2 = [11,1,3,4,5,4,3]
numbers2_duplicates_removed = remove_duplicates(numbers2)
print(numbers2_duplicates_removed)

count = 10
increment()
print(count)

addWithUnlimitedParameter(2,3,4,5,6,7,8,9,10)