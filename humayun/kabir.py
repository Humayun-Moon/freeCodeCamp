class Items:
    # with 30% Discount
    discount = 0.70 
    item_all = []
    def __init__ (self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity 
        Items.item_all.append(self)
    def get_total (self):
        total = self.price * self.quantity
        print(f"Your total price : {total}")
    def get_average (self):
        average = (self.price * self.quantity) / self.quantity 
        print(f"Your Average price per {self.name} : {average}")
    def total_price_discount (self):
        get_total_discount = (self.price * self.quantity) * 0.7
        print(f"You total price with discount : {get_total_discount}") 

    def __repr__(self):
        return f"Items({self.name}, {self.price}, {self.quantity})"    
name = input("Enter you product name : ")
price = int(input("Enter each price of your prouduct: "))    
quantity = int(input("Enter Quantity : "))
item1 =Items(name, price, quantity)
# item2 =Items("Mobile", 1987, 12)
# item3 =Items("Computer", 4980, 14)
# item4 =Items("Laptop", 7686, 29)
print(f"Here is {item1.name} ")
item1.get_total()
item1.get_average()
item1.total_price_discount()
print("---------------------------")

# print(f"Here is {item2.name} ")

# item2.get_total()
# item2.get_average()
# item2.total_price_discount()
# print("---------------------------")
# print(f"Here is {item3.name} ")

# item3.get_total()
# item3.get_average()
# item3.total_price_discount()
# print("---------------------------")
# print(f"Here is {item4.name} ")

# item4.get_total()
# item4.get_average()
# item4.total_price_discount()
# print("---------------------------") 

print(Items.item_all) 

print("-------------------------------------") 

for intance in Items.item_all:
    print(f"{intance.name}:  {intance.price} ----- {intance.quantity}")
