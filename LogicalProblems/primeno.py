# To check whether the number is prime or not
# A prime number is not divisible on any number except on its own table.
n=int(input("Enter a number: "))

    
if n<=1:
    print("Not a prime number")
else:
    for i in range(2,n):
        if n%i==0:
            print("Not a prime number")
            break
    else:
        print(f"{n} is a prime number")