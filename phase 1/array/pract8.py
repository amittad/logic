#8. Find the index of the maximum element. 
arr=[10,2345,3,4,511,6,33,1,22,67]
max=arr[0]
a=0
for i in arr:
    if i>max:
        max=i
        
print(arr.index(max))            