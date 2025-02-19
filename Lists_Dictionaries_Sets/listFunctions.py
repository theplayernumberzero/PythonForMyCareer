fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']

print(len(fruits)) # 5

#adding elemnet to index which we want
fruits.insert(2, 'blueberry')
print(fruits) # ['apple', 'banana', 'blueberry', 'cherry', 'date', 'elderberry']

#adding element to the end of the list
fruits.append('fig')
print(fruits) # ['apple', 'banana', 'blueberry', 'cherry', 'date', 'elderberry', 'fig']

#adding list to list
fruits.extend(['grape', 'honeydew'])
print(fruits) # ['apple', 'banana', 'blueberry', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew']

#removing element from list
fruits.remove('date')

#removing elemnet of last index
fruits.pop()

#print index of element
print(fruits.index('banana')) # 1

scores = [10, 20, 30, 40, 50, 60, 70, 80, 100, 90]

#max value of list
print(max(scores)) # 100

#concetenate list
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list1 + list2
print(list3) # [1, 2, 3, 4, 5, 6]

#multiply list
list4 = list1 * 3
print(list4) # [1, 2, 3, 1, 2, 3, 1, 2, 3]

#mutability
list1[0:3] = [8,9,10]
print(list1) #8,9,10