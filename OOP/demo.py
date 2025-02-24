class Product:
    #class variable
    brand = "Adel"
    
    def __init__(self, name, price):    #self is reference to the current object
        self.name =name
        self.price = price

    def summer_discount(self):
        self.price = self.price * 0.5

    #class method(instead of self, we use cls)
    @classmethod
    def showClassVariable(cls):
        print(cls.brand)

    #static method
    @staticmethod
    def add(a,b):
        print(a+b)

#inheritance
class DigitalProducts(Product):

    #Superclassın init func kullanıp, attributelarına değer atıyoruz
    def __init__(self, name, price, link):
        super().__init__(name, price)   #superclass methodu kullanırken super() keywordu kullanlır
        self.link = link

    #override method
    def summer_discount(self):
        self.price = self.price * 0.8   #super class att kulanırken sub class kendi attrübute imiş gibi davranabilir


p1 = Product("kalem", 5)
p2 = Product("silgi", 3)

print(p1.name)
print(p1.price)

p1.summer_discount()

print(p1.name)
print(p1.price)

print("----")

print(p2.name)
print(p2.price)

print("----")

ebook = DigitalProducts("ebook", 10, "www.ebook.com")
print(ebook.name)
print(ebook.price)
print(ebook.link)

ebook.summer_discount()
print(ebook.price)

print(ebook.brand)

Product.add(3,10)