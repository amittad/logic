#Find the maximum and minimum element in an array. 
nums=[2,1,4,6,7,3,9,65,23,45]
small=nums[0]
big=nums[0]
for num in nums:
    if big<num:
        big=num
    if small>num:
        small=num
print(big,small)            
        