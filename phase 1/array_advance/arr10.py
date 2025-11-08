#Copy one array to another manually. 
arr = [1, 2, 3, 4,5,6]   
arr2=[0]*len(arr)
for i in range(0,len(arr)):
    arr2[i]= arr[i]
print(arr2)    