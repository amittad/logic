 #Print first n terms of a geometric progression (a, r). 
n=int(input("enter a number for range"))
a=int(input("enter a number "))
b=int(input("enter a number for differance"))
for i in range(a,n+1):
    print(a)
    a=a*b
    
