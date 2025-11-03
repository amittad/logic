#5. Find the minimum element in an array
arr=[10,2,3,4,51,6,33,1,22,67]
min=arr[0]
for i in arr:
    if min>i:
        min=i

print(min)   