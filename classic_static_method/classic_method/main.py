import os
import csv

class Items:
    bonus = 0.2 
    all_items = []
    def __init__(self,group_name:str,count:int,salary:int):
        
        
        self.group_name = group_name
        self.count = count 
        self.salary = salary
        Items.all_items.append(self)
    def total_salary (self):
        total = self.count * self.salary
        print("Total salary :",total)
    def average_salary (self):
        average = (self.count * self.salary) / self.count
        print("Average salary : ",average) 
    def salary_with_bonus (self):
        salary_bonus = self.salary * Items.bonus
        salary_with_bonus = salary_bonus + self.salary
        print("Salary with bonus each group: ", salary_with_bonus) 
    def __repr__(self):
        return f"Items({self.group_name}, {self.count}, {self.salary})"      
    @classmethod    
    def instantite_from_csv (cls):
        with open("items.csv", "r")  as f:
            reader = csv.DictReader(f)  
            items =list(reader)
        for item in items:
            print(item)    
Items.instantite_from_csv()
item1 = Items("Production", 100, 12000 )


# item2 = Items("Loder", 50, 10000 )
# item3 = Items("Quality", 70, 16000 )
# item4 = Items("Human-Resource", 10, 30000 )
# item5 = Items("Maintainece", 5, 15000 ) 
# print("---------------------------------------------")
# print(f"Below the information of Group {item1.group_name}")
# item1.total_salary()
# item1.average_salary()
# item1.salary_with_bonus() 
# print("---------------------------------------------")


# print(f"Below the information of Group {item2.group_name}")

# item2.total_salary()
# item2.average_salary()
# item3.salary_with_bonus()
# print("---------------------------------------------")


# print(f"Below the information of Group {item3.group_name}")

# item3.total_salary()
# item3.average_salary()
# item3.salary_with_bonus()
# print("---------------------------------------------")


# print(f"Below the information of Group {item4.group_name}")

# item4.total_salary()
# item4.average_salary()
# item4.salary_with_bonus() 
# print("---------------------------------------------")


# print(f"Below the information of Group {item5.group_name}")

# item5.total_salary()
# item5.average_salary()
# item5.salary_with_bonus() 
# print("---------------------------------------------")


# get_all_items = Items.all_items
# print(get_all_items) 

# for intence in get_all_items:
#     print(f"{intence.group_name} : {intence.count} : {intence.salary}") 

current_dir = os.getcwd()
print(current_dir)

