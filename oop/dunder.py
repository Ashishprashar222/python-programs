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
    @classmethod
    def from_str(cls,empstr):                                    #class method as alternative constructor
        fname,lname,salary=empstr.split("-")
        return cls (fname, lname, salary)
    @staticmethod
    def isopen(day):
        if day =="sunday":
            return False
        else:
            return True 

akash=company("Akash","raj",2500)
atul=company("Atul","chandra",25)