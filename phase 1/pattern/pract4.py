#Print a Right-Aligned Triangle of Stars
n = int(input("Enter n: "))   # e.g. 5
for i in range(1, n+1):
    print(" # " * (n-i)+"*" * i)
