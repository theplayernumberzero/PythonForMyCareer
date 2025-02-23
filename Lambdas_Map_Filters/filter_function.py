#filter func: filtreleme işlemi yapar, sadece True dönen elemanları alır
#Map listenin tüm elemanlarına işelm yaparken, filter sadece trur dönen elemanları alır

def check_even(x):
    return x%2 == 0

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers)

even_numbers = list(filter(check_even, numbers))
print(even_numbers)