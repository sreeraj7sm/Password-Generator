from random import choice 

a=int(input('What should be the lenght of the password?'))
small='abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*'
password=''

for i in range(a):
    password += choice(small)
print(password)