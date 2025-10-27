#Print numbers between 1–100 whose digits add up to a multiple of 3. 
for i in range(1,101):
    temp=i
    revese=0
    while temp>0:
       
        revese += temp % 10   # Add last digit
        temp = temp // 10 
    if revese%3==0:
        print(i)    
