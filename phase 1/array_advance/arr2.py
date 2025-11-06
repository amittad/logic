#2. Count how many times a given element appears. 
arr=[1,2,3,4,2,5,8,9,34,56]
count=0
num=int(input("enter a number to find element in how many time in array="))
for i in arr:
    if num==i:
        count+=1
print(count)        