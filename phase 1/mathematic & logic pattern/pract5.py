n=int(input("enter a number for range"))
a=int(input("enter a number"))
b=int(input("enter a number"))
ar=[]
br=[]

for i in range(1,n+1):
    ar.append(a*i)
    br.append(b*i)
   
for i in ar:
    for j in br:
        if i==j:
            print(i)
