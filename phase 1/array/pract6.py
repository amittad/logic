#6. Count how many elements are positive, negative, or zero. 
arr=[1,2,3,4,51,6,33,22,-7,-2,-43,0]
neg=0
poe=0
for i in arr:
    if i<=0:
        neg+=1
        print(i)
    else:
        poe+=1    
        print(f"positive{i}")
print(neg)  
print(poe)      