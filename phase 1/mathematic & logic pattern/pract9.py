#Print first n terms of an arithmetic progression (a, d). 

n=int(input("enter a number for range"))
a=int(input("enter a number "))
b=int(input("enter a number for differance"))
for i in range(a,n+1,b):
    print(i)
