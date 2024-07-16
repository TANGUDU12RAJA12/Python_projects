import random
import string
password_len = 5
charValues = string.ascii_letters + string.digits + string.punctuation
#m2
#list comprehension [function for i  in rage(n)]
#"".JOIN METHODE IS RETURN A NEW STRING WITHOUT LIST TYPE
result = "*".join([random.choice(charValues) for i in range(password_len)])
print("your randam password is :",result) 




"""m1"""
#password = ""
#for i in range(password_len):
    #print(random.choice(charValues))
    #password += random.choice(charValues)

#print("your randam password is :",password)    













# GENERATE THE ALL ENGLISH CHARACTER
#print(string.ascii_letters)
# GENERATE THE ALL DIGITS
#print(string.digits)
# GENERATE THE ALL SPECIAL CHARACTER
#print(string.punctuation)
#val = random.choice(["a","b","c"])
#print(val)
