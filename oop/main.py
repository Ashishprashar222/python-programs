class company:                                              #class
    increment = 1.5
    no_of_worker= 0                                
    def __init__(self,fname,lname,salary):                     #constructor
        self.fname=fname
        self.lname=lname
        self.salary=salary
        company.no_of_worker +=1
    def increase(self):
        self.salary = self.salary * self.increment   
    @classmethod                                            #using claass mehods
    def change_increment(cls,amount):
        cls.increment=amount   
sonal=company('sonal','sarkar',20000)             #Object 
dhaka=company('dhaka','suresh',30000)

print(dhaka.fname,dhaka.lname,dhaka.salary)
print(sonal.fname,sonal.lname,sonal.salary)
dhaka.increase()
print(dhaka.salary)
print(company.no_of_worker)
company.change_increment(3)             #using Change_increment function
dhaka.increase()                                 #calling increase function
print(dhaka.salary)