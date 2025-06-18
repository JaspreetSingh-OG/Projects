def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
n=int(input("Enter the number: "))
for i in range(n):
    print("Fibonacci series: ",fibonacci(i))
# print(f"The sum of {n} fibonacci series is: {fibonacci(n)}")