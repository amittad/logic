num=int(input("enter  a number="))
s=num
store=[]

for i in range(1,num):
    a=i
    sum=0
    for j in range(1,i):
        if a%j==0:
            sum+=j
    if sum==i:
        store.append(i)     

print(f"total perfect number between 1 to {num} is {store}")


