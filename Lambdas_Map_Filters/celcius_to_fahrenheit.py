celcius = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(celcius)

fahrenheit = list(map(lambda x:x*1.8 +32, celcius))
print(fahrenheit)