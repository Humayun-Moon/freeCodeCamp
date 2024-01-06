class Salary:
    item = []
    def __init__(self,name:str,id:int,old_salary:int, new_salary:int):


        self.name = name
        self.id = id
        self.old_salary = old_salary
        self.new_salary = new_salary 
        Salary.item.append(self)

        assert old_salary >= 10000
        assert new_salary >= 13500
    def employee_info(self):
        print(f"The employee {self.name} and id number {self.id} old salary was {self.old_salary} and he'll get new salary in per month {self.new_salary}")    
    def salary_increasment_ratio (self):
        percent = (self.new_salary - self.old_salary)/ 100
        return percent 
    def old_basic (self):
        basic_old = self.old_salary *0.47
        return basic_old
    def new_basic (self):
        basic_new = self.new_salary * 0.47
        return basic_new   
# user input     
name = input("Enter your name : ") 
id = int(input("Enter your ID number : "))
old_salary = int(input("Enter the old salary : "))
new_salary = int(input("Enter the new salary: ")) 

# declear class 
em1 = Salary(name,id , old_salary, new_salary ) 

em1.employee_info() 

grow_percent =em1.salary_increasment_ratio()
print(f"The employee of {em1.name} has been salary increment {grow_percent}%")

old_basic = em1.old_basic()
new_basic = em1.new_basic()

print(f"You old basic salary was {old_basic} and you'll get new basic salary {new_basic}")

print("Your all info is here ",Salary.item)    