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

        file = open(self.__file_name, 'r')
        info_ = file.read()
        #pprint(file.read())
        file.close()
            #prod_.join(info_)
        return info_
    def add(self, *products):
        file_ = open(self.__file_name, 'a')
        file_info = self.get_products()
        for prod in products:
            if prod.name in file_info:
                print(f"Продукт {prod.name} уже есть в магазине") # обрадуемся к имени продукта в Class Products
            else:
                file_.write(str(prod)+ '\n')
        file_.close()




s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())

