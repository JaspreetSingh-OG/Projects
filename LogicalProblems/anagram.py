def anagram(s1,s2):
    s1=s1.replace(" ","").lower()
    s2=s2.replace(" ","").lower()

    if sorted(s1)==sorted(s2):
        return True
    else:
        return False
    
s1=input("Enter the string: ")
s2=input("Enter the string: ")

if anagram(s1,s2):
    print("This string is an anagram")
else:
    print("This string is not an anagram")