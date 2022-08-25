import random

length_passwrd = int(input("enter the length of password: \n"))
all_chrcter = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
password = "".join(random.sample(all_chrcter,length_passwrd))
print(password)