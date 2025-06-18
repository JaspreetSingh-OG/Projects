#A program to check whether the number is even or odd!
# An Even number is always divisible by 2 and its remainder comes 0 while odd numbers aren't divisible by 2 and their remainder is not 0 on dividing with 2
def odd_even():
    n=int(input("Enter the number: "))
    if n%2==0:
        print(f"{n} is an even number")
    else:
        print(f"{n} is an odd number")
odd_even()