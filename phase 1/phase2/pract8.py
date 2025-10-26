store=[]

for i in range(1,100000):
    num=i
    n=len(str(i))
    add=0
    while num>0:
        last=num%10
        add+=last**n
        num//=10
    
    if i == add:
        store.append(i)    
print(store)    