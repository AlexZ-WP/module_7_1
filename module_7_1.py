
from pprint import pprint

class Product:

    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    __file_name = 'products.txt'
    def get_products(self):
        __file_name = 'products.txt'
        file = open(__file_name, 'r')
        pprint(file.read())
        file.close()


    def add(self, *products):

        for i in products[0:]:
            if i == products:
                __file_name = 'products.txt'
                file = open(__file_name, 'a')
                file.write()
                file.close()
            break
        else:
            return

        print("Продукт  уже есть в магазине")


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())




s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')

p2 = Product('Spaghetti', 3.4, 'Groceries')

p3 = Product('Potato', 5.5, 'Vegetables')
#
print(p2) # __str__
#
# s1.add(p1, p2, p3)

print(s1.get_products())

# s1=Shop()
# # products = []
# #
# #     def __new__(cls, *args, **kwargs):
# #         cls.products.append(args[0])
# #         return object.__new__(cls)
#
# print(s1.get_products())