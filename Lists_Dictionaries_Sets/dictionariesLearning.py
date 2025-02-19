#dictionaries: You can store complex data
#collection of key and value pair
#keys are unique

cities = {"Ankara":6, "İstanbul":34}
print(cities)

#get value
print(cities["Ankara"])

#dictionaries are mutuable, you can change value
cities["İstanbul"] = 340

#creating dictionaries with dict() not : use =
ages = dict(
    bahadir=23,
    meltem=14
)

#adding new key-value to dict
ages["mehtap"] = 19
print(ages)

#remove pair
del ages["mehtap"]
print(ages)

#get method: If there is no key as arguemnt get() return None
print(ages.get("bahadir"))
print(ages.get("elif")) #None

#update
prices = {"ipad":100, "iphone":200}
new_prices = {"iphone":300, "imac":400}

prices.update(new_prices)
print(prices)

#pop
prices.pop("imac")
print(prices)

a = prices.pop("iphone")
print(prices)
print(a)

#values()
ages2 = {"ali" : 1,"mehmet": 2}
print(ages2.values())

#keys()
print(ages2.keys())

#items(): return all pairs as element
print(ages2.items())