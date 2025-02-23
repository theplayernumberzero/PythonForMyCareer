#liste elemanlarına teker teker manipüle etme imkanı verir

def square(x):
    return x**2

numbers = [1, 2, 3, 4, 5]
print(numbers)

new_numbers = list(map(square, numbers))    #sadece func adını yaz
print(new_numbers)

#%10 indirim
prices = [100, 200, 300, 400, 500]
print(prices)

#İlk olarak elemanlara uygulamak istediğin işlemi ver, sonra hangi listenin elemanlarına işlem yapmak istediğini belirt
new_prices = list(map(lambda x: x*0.9, prices))
print(new_prices)
