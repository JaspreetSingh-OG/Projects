
def armstrong():
    a=int(input("Enter a number: "))
    x=a//100
    y=(a//10)%10
    z=a%10
    result=lambda x,y,z:x**3+y**3+z**3
    if a==result(x,y,z):
        print("This number is armstrong")
        return result
    else:
        print("This number is not armstrong")
armstrong()
    

    

