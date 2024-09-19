import random
password="ABCDEFG12345abdcefg!@#$%{}<>"
length_password=int(input("Enter the length of the password :"))
a="".join(random.sample(password,length_password))
print(f"your password is{a} ")
