import string
import random

len=int(input("Enter length of password: "))
"""
lower= string.ascii_lowercase
upper=string.ascii_uppercase
digits= string.digits
symbols=string.punctuation

str=lower+upper+digits+symbols
"""
str=string.printable
pwd=random.sample(str,len)
password="".join(pwd)
print("output:- "+password)
print(str)
