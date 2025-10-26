n=int(input("enter a number for range"))
store_n=n
add=0
while store_n>0:
    last=store_n%10
    a=last
    fact=1
    print(last)
    for i in range(1,last+1):
       fact*=i
    add+=fact   

    store_n //=10
print(add)
if n==add:
    print(n, "is a Strong Number")
else:
    print("not strong number")    