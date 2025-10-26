n=5125
add=0
while n>0:
    last=n%10
    add+=last
    n//=10
print("addition sum of number is=",add)    
