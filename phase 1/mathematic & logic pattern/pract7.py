#Find the sum of all factors of a number. 
n=int(input("enter a number for range"))
a=n
sum=0
for i in range(1,n+1):
    if a%i==0:
        sum+=i
print(f"sum of facto is = {sum}")        