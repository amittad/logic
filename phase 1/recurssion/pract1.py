#1 . Print numbers from 1 to n using recursion. 
def countdown(n):
    if n==0:
        return 
    
    countdown(n-1)  
    print(n)  
countdown(5)        