#syntax errors
#logical errors
#runtime errors
#exception handling

#try except blocks
#sorun çıkarabilecek kodu try içine alıyoruz. It checks for eroros and exceptions
#except is belirtilen hata olduğunda ne yapacağını belirlediğin yer


n = int(input("Enter a number: "))
d = int(input("Enter a number: "))
result = 0

try:
    result = n/d
except ZeroDivisionError:   #we handled runtime error
    print("You cant divide by zero")
else:  #if there is no error or exceptions
    print(result)
finally:    #hata olsa da olmasa da çalışacak kodları buraya yazıyoruz
    print("This code will be executed no matter what")
