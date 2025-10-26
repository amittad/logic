num =int(input("enter a range of number to find this numbers is palindrome"))
product = 0
store=[]
nonpali=[]
for i in range(1,num+1):
    temp = i          
    reverse = 0
    while temp > 0:
        digit = temp % 10
        reverse = reverse * 10 + digit
        temp //= 10

    if i == reverse:
        store.append(i)
    else:
        nonpali.append(i)

print(store)
print(nonpali)        