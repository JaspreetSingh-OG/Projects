#Using Function
# def factorial(n)->int:
#     result=1
#     for i in range(1,n+1):
#         result*=i #multiplies the value of result with i then assign it to result
#     return result
# n=int(input("Enter a number: "))
# print(f"The factorial of {n} is : {factorial(n)}")

#Using Recursion
def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)
n=int(input("Enter a number: "))
print(f"The factorial of {n} is : {factorial(n)}")


    

