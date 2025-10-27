nums=[1,3,5,7,6,4,9]
m=max(nums)
s=min(nums)
arr=[]
for i in range(s,m+1):
    if i not in nums:
        arr.append(i)
print(arr,"this numbers is missing")