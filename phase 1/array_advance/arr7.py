#7. Find the sum of odd elements only. 
arr=[10,2,3,4,51,6,33,1,22,67]
add=0
for i in arr:
    if i%2!=0:
        add+=i
print(add)
