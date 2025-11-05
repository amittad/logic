#. Take n elements and print only those greater than a given value k. 
sizeofarr=int(input("enter a size of array"))
arr=[]
for i in range(sizeofarr):
    n=int(input("enter a number "))
    arr.append(n)
print("enter a number grether than given value=")
num=int(input("enter a number="))
for i in arr:
    if num<i:
        print(i)    

