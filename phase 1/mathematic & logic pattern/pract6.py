#. Print all factors of a given number
n=int(input("enter a number for range"))
a=n
for i in range(1,n+1):
    if a%i==0:
        print(i)