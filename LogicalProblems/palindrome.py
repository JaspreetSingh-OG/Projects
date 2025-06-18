def palindrome(s):
    return s==s[::-1] # Used for reversing a string
word=input("Enter a String: ")
if palindrome(word):
    print("This string is a palindrome!")
else:
    print("This string is not a palindrome")
    