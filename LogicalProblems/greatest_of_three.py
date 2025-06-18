# To find greatest of 3 numbers entered by a user, we'll use conditional statements and a function.
def greatest()->int:
    a=int(input("Enter the number: "))
    b=int(input("Enter the number: "))
    c=int(input("Enter the number: "))
    if (a>b) and (a>c):
        print(f"{a} is the greatest number!")
    elif (b>a) and (b>c):
        print(f"{b} is the greatest number!")
    elif (c>a) and (c>b):
        print(f"{c} is the greatest number!")
    else:
        print("All Numbers are Equal")
greatest()