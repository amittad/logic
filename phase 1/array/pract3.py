#3. Find the average of array elements.
arr=[1,2,3,4,5,6,33,22]
a=len(arr)
avg=1
sum=0
for i in arr:
    sum+=i
avg=sum//a    
print(avg)