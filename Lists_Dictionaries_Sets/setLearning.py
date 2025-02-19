#set type: Collection of elements which are unique
#sets are unordered and you cant get index of element
numbers = set([1,2,3,4])
print(numbers)

numbers2 = {1,2,3,4,3} #eliminate oto last 3
print(numbers2)

#create a empty set
s = set()
print(s)

#check valur is in set
print(1 in numbers) #True

#union interseciton and different of set
seta = {1,2,3,4,5}
setb = {4,5,6,7,8}

print(seta | setb) #union of sets
print(seta & setb) #intersection of sets
print(seta - setb) #difference of sets
print(seta ^ setb) #remove intersection and combine them

#adding elemnt to a set
seta.add(10)
print(seta)

#remove element from set
seta.remove(2)
print(seta)

#discard() : Same with remove() but if there is no such a element this one dont give error
seta.discard(100)
print(seta)

#pop() : remove random element from set
seta.pop()
print(seta)

#clear() : Remove all elemnts from set
seta.clear()
print(seta)