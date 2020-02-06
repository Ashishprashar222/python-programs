class student:
    increment=2
    def __init__(self,fname,lname,salary):
        self.fname=fname                                            #constructor
        self.lname=lname
        self.salary=salary
    def incerments(self):
        self.salary=int(self.salary * self.increment)
    @classmethod
    def funcname(self,amount):
        cls.increment=amount

    @classmethod
    def from_str(cls,empstr):                                    #class method as alternative constructor
        fname,lname,salary=empstr.split("-")
        return cls (fname, lname, salary)
        

soanl=student('sonal','sarkar',500)
dhaka=student('dhaka','suresh',800)
print(dhaka.fname,dhaka.lname,dhaka.salary)
dhaka.incerments()
print(dhaka.salary)
ashish=student.from_str("ashish-kumar-1200")
print(ashish.lname)

class subject(student):
    def __init__(self,fname,lname,slary,prglang,exp):
        super().__init__(fname,lname,salary)
        self.prglang=prglang
        self.exp=exp
akash=subject("Akash","raj",2500,'python','5 yrs')

print(akash.exp)