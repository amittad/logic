#4. Find HCF (GCD) of two numbers using loops. 
a=int(input("enter a number"))
b=int(input("enter a number"))
c=min(a,b)
add=1
for i in range(1,c+1):
    if a % i==0 and b % i==0:
        add=i

print(add)        