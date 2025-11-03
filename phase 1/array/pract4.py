#4. Find the maximum element in an array
arr=[1,2,3,4,51,6,33,22,67]
max=arr[0]
for i in arr:
    if max<i:
        max=i

print(max)        