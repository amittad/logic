#7. Count how many elements are even and odd. 
arr=[10,2,3,4,51,6,33,1,22,67]
even=0
odd=0
for i in arr:
    if i%2==0:
        print("even",i)
        even+=1
    else:
        print("odd",i)    
        odd+=1
print(even)
print(odd)        