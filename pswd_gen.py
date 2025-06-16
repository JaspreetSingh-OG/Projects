import string
import random
n=int(input("Enter Password Length: "))
characters=string.ascii_letters+string.digits+string.punctuation
password=''.join(random.choice(characters) for i in range(n))
print(f"Generated Password: {password}")