#This program will detect the vowels in a string.
text=input("Enter the String: ").lower()
vowels="aeiou"
found_vowels=set()
count=0
for ch in text:
    if ch in vowels:
        found_vowels.add(ch)
        count+=1
print(f"Given string contains {count} vowels")
print(f"Vowels found: {', '.join(sorted(found_vowels))}")