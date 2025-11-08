#Swap alternate elements (1st ↔ 2nd, 3rd ↔ 4th, etc.). 
arr = [1, 2, 3, 4,5,6]    
for i in range(0,len(arr)-1,2):
   arr[i+1],arr[i]= arr[i],arr[i+1]
print(arr)     
