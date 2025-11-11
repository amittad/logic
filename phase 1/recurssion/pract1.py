#1 . Print numbers from 1 to n using recursion. 
def countdown(n):
    if n<=0:
        print("done")
    else:
        print(n)
        countdown(n-1)    
countdown(5)        