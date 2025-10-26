#. Print all numbers between a and b divisible by 7
a=int(input("enter a number"))
b=int(input("enter a number"))
for i in range(a,b):
    if i%7==0:
        print(i)