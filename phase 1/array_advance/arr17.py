'''एक list दी गई है:
[12, 7, 35, 22, 18, 5, 3, 101, 44]
इसमें से prime numbers, even numbers, odd numbers अलग 3 lists में store करो and print highest prime'''

l1=[12, 7, 35, 22, 18, 5, 3, 101, 44]
odd=[]
even=[]
prime=[]
for i in l1:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)    
for i in l1:

    if i > 1:               
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            prime.append(i)              
print(even)   
print(odd)
print(prime)    
print(max(prime))     