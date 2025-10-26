num=int(input("enter  a number="))
fact=1
for i in range(1,num+1):
    fact*=i

facto=[x for x in range(1,num+1)]    
print(facto,fact)