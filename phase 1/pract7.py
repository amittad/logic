num=int(input("enter  a number="))
add=0
for i in range(1,num+1):
    if i%2==0:
        add+=i

print(add)        
addd=[i for i in range(num) if i%2==0]
print(addd,add)