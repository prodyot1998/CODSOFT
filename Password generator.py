import random
import string
def generatepassword(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
p=int(input(" Enter the password length"))
if (p < 0) :
    print("Invalid Length!!")
q=generatepassword(p)
print(q)