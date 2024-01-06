import os 
import io 

# current_dir = os.getcwd()
# print(current_dir) 

# if (not os.path.exists("data")):
#     os.mkdir("data/my_file.txt")
# with open("data/my_file.txt", "w") as f:
#     f.write("This is my file")
# f.close()   


# import csv

# class Items:
#     all_items = []
#     def __init__(self,name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity 
#         Items.all_items.append(self)

#     def show_info (self):
#         print(f"The name of prouduct is {self.name} price {self.price} and it has {self.quantity}")    
#     def total_price (self):
#         total = self.price * self.quantity
#         print(f"Your total price is : {total}")  
#     def average_price (self):
#         average = (self.price * self.quantity)/ self.quantity 
#         print(f"Your average price is : {average}") 
#     def __repr__(self):
#         return f"Items({self.name}, {self.price}, {self.quantity})"
    
#     @classmethod
#     def import_from_csv (cls):
#         with open("items.csv", "r") as f:
#             reader =csv.DictReader(f)
#             items = list(reader)
#         for item in items:
#             print(item)
#             Items(
#                 name=item.get('name'),
#                 price=item.get('price'),
#                 quantity=item.get('quantity')
#             )    
# Items.import_from_csv() 
# print(Items.all)       
import csv
import os

class Items:
    all_items = []

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity 
        Items.all_items.append(self)

    def show_info(self):
        print(f"The name of product is {self.name}, price {self.price}, and it has {self.quantity}")

    def total_price(self):
        total = self.price * self.quantity
        print(f"Your total price is: {total}")

    def average_price(self):
        average = (self.price * self.quantity) / self.quantity
        print(f"Your average price is: {average}")

    def __repr__(self):
        return f"Items({self.name}, {self.price}, {self.quantity})"

    @classmethod
    def import_from_csv(cls):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        csv_path = os.path.join(script_dir, "items.csv")
        
        with open(csv_path, "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            print(item)
            Items(
                name=item.get('name'),
                price=item.get('price'),
                quantity=item.get('quantity')
            )

Items.import_from_csv() 
print(Items.all_items)
# print(Items.all)    

        
item1 = Items("Mobile", 2000, 10)              
item2 = Items("Computer", 5000, 20)              
item3 = Items("Keyboard", 1000, 20)              
item4 = Items("Monitor", 3200, 12) 

item1.show_info()
item1.total_price()
item1.average_price()

print("----------------------")

item2.show_info()
item2.total_price()
item2.average_price()

print("----------------------")

item3.show_info()
item3.total_price()
item3.average_price()
print("----------------------")

item4.show_info()

item4.total_price()
item4.average_price()
print("----------------------")

get_all_items = Items.all_items
print(get_all_items) 

# for item in get_all_items:
#     print(item)
