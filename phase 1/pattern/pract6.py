#8. Print Stars in Odd Numbers (1, 3, 5, 7, 9)
n=int(input("enter a number="))
for i in range(1,n+1,2):
    for j in range(i):
        print("*", end="")
    print(" ")    
    
        