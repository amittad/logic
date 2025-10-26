n=int(input("enter a number"))
a=0
b=1
add=0
for i in range(n):
    print(a)
    add+=a;
    c=a+b
    a=b
    b=c
print(add)