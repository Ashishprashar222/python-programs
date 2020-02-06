from time import time

def fun1(a,b):
    return a+b
    
def fun2(a,b):
    num1= a
    num2= b
    return (a+b)


if __name__ == "__main__":
    init = time()
    #fun1(3,5)
    print(fun1(3,5))
    print("fun1",time()- init)
    init=time()
    print(fun2(4,3))
    print("fun2",time() - init)