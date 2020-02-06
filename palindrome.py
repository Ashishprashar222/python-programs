'''number=int(input("enter the number"))
reverse=0
temp=number
while(number>0):
    reminder =number%10
    reverse=(reverse*10)+reminder
    number=number//10
print("reverse is= ",reverse)

if temp==reverse:
    print("palindrome")
else:
    print("not palindrome")'''


'''**************************************************************************************************'''
def checkpalindrome(number):
    temp=number
    reverse=0
    while(number>0):
        remainder=number%10
        reverse=reverse*10+remainder
        number=number//10
    print(reverse)
    if temp==reverse:
        print("palindrome")
    else:
        print("not palindromes")


number=int(input("enter the number:"))
print(checkpalindrome(number))