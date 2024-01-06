class Person:
    all_info = []
    def __init__(self,name, age, occu, aimbation):
        self.name = name
        self.age = age
        self.occu = occu
        self.aim = aimbation 
        Person.all_info.append(self)
    def info (self):
        print(f"{self.name} is {self.age} years old. At present, He/she working for {self.occu}. But, He/she is also aimbation is {self.aim} ")
    def __repr__(self):
        return f"Person({self.name}, {self.age}, {self.occu}, {self.aim})"    
        

p1 = Person("Humayun", 24, "Self and Skill Development", "Be a honest person and also become a software Developer")
p2 = Person("Humayun", 24, "Self and Skill Development", "Be a honest person and also become a software Developer")
p3 = Person("Humayun", 24, "Self and Skill Development", "Be a honest person and also become a software Developer")
p4 = Person("Humayun", 24, "Self and Skill Development", "Be a honest person and also become a software Developer")
p5 = Person("Humayun", 24, "Self and Skill Development", "Be a honest person and also become a software Developer")
p6 = Person("Humayun", 24, "Self and Skill Development", "Be a honest person and also become a software Developer")
p7 = Person("Humayun", 24, "Self and Skill Development", "Be a honest person and also become a software Developer")
# p1.info()
# print("---------------------------")
# p2.info()
# print("---------------------------")
# p3.info()
# print("----------------------------")
# p4.info()
# print("----------------------------")
# p5.info()
# print("---------------------------")
# p6.info()
# print("---------------------------")
# p7.info()
# print("---------------------------------------")

all_info_person = Person.all_info
print(list(all_info_person))


for instance in Person.all_info:
    print(f"{instance.name} , {instance.age}, {instance.occu}, {instance.aim}")
