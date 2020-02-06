from time import time
if __name__ == "__main__":
    init=time()
    
    num=int(input("Enter the number"))
    fact=1
    if num<0:
        print("Wrong input")
    elif num==0:
        print("1")
    else:
        for i in range(1,num+1):
            fact=fact*i
        print("factorial of a num",fact)
    print(time()- init)
    a=input()
