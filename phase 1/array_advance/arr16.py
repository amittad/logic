even=[]
odd=[]
for i in range(1,101):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
store=[]
l=len(odd)
for i in range(1,l):
    a=even[i]+odd[i]
    print(f"{even[i]}+{odd[i]}=={even[i]+odd[i]}")
   