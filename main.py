# class Item:
#     def get_total_price (self,name,price,quantity):
#         total_price = price * quantity
#         return total_price 
#     def average_price (self, name,price, quantity):
#         get_average = price / quantity
#         # return get_average 
#         print(f"The average price is : ", get_average)




# item1 = Item()
# item1.name = "iPhone"
# item1.price = 2000
# item1.quantity = 33
# get_total_price = item1.get_total_price(item1.name, item1.price, item1.quantity)
# print("Total Price is :",get_total_price)
# get_average = item1.average_price(item1.name, item1.price, item1.quantity) 


class Items:
    # The pay rate after 20% discount
    pay_rate = 0.7 
    def __init__(self,name= str,price = int, quantity= int):
        # Assign to self object  
        self.name = name
        self.price = price
        self.quantity =  quantity 
        # Run Validation to recevied arguments 
        assert self.price >= 0, f"Price isn't grether than zero!"
        assert self.quantity >=0, f"Quaintity isn't grether than zero"
    def calculate_total_price (self):
        return self.price * self.quantity    

    # def info(self):
    #     print(f"{self.name} has stored of {self.quantity} each price is {self.price} ")    
    def get_total (self):
        return self.price * self.quantity 
    def discount_get (self):
        average = self.price * self.quantity
        discount = average * self.pay_rate
        return discount

# a = Items()
i = Items("Mobile", 1000, 50)        
i1 = Items("Laoptop", 1000, 50)        
i2 = Items("Desktop", 2001, 50) 

total_price = i.calculate_total_price()
print("Your total price is : ",total_price)
print("--------------") 
get_total_discount = i.discount_get()
print("You total price with discount is : ", get_total_discount) 

print("--------------------------")

i1.pay_rate = 0.7
total_price = i1.calculate_total_price()
print("Your total price is : ",total_price)
print("--------------") 
get_total_discount = i2.discount_get()
print("You total price with discount is : ", get_total_discount) 




# All atributes for Class level 
# print(a.__dict__)
# print("------------")
# print(i.__dict__)
# print(i1.__dict__)
# print(i.pay_rate)     
# print(i1.pay_rate)     
# print(i2.pay_rate)     
# class AddInfo(Items):
#     def __init__(self,name,price,quantity,storeName,address):
#         super().__init__(name,price,quantity)
#         self.storeName = storeName
#         self.address = address
#     def update_info (self):
#         print(f"{self.name} has stored of {self.quantity} each price is {self.price} Our showroom name is {self.storeName} near by {self.address} ")    

                



# name = input("Enter the name of prouduct : ")
# prouduct_price = int(input("Enter the price to buy : "))
# prouduct_quantity = int(input("Enter the Quantity to buy : "))
print("--------------------------------------")    
# i = Items(name,prouduct_price, prouduct_quantity)
# print("Your total price is : ",i.get_total())
# print("-------------------")
# print(i.calculate_total_price()) 


# ui1 = Items("Laptop", 3999, 50)
# print(ui1.get_total())
# print(i.name)


# ui = AddInfo() 
# # ui1 = AddInfo("Laptop", 3999, 50, "khusbu Enterprize", "Norshindhi, Dhaka")
# # # ui.update_info()
# # ui1.update_info()