n=int(input("enter a number for check number is armstrong and not"))
dupli=n
mult=0
add=0
while dupli>0:
    num=dupli%10
    mult+=num*num*num
    dupli//=10
if n==mult:
    print(f"{n}=={mult} this number is armstrong")   
else:
    print(f"{n}=={add} this number is not armstrong")  

