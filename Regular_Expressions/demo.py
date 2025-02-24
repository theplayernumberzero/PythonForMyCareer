#regular expression, belirli desenlerle metinleri analiz etmeye, aramaya ve değiştirmeye yarayan bir araçtır.
#for use it import re module
#is particular pattern has in string we check it

import re

print("This is \nnot raw string")
print()
print(r"this is \n raw string") #disable special characters

string = "bac"
pattern = "a"
#we can do complex search also
if re.match(pattern=pattern, string=string): #return object or none(look for only first character)
    print("Match found")
else:
    print("Match not found")

#match vs search
if re.search(pattern=pattern, string=string): #return object or none(look for entire string)
    print("Match found")
else:
    print("Match not found")

