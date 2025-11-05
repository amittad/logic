#9. Find the index of the minimum element. 
arr=[11,2,3,4,51,6,33,22,67]
min=arr[0]
for i in arr:
    if i<min:
        min=i
print(min)
print(arr.index(min))        