num = 212
ex=num
product = 0
while num > 0:
    digit = num % 10
    product=product*10+digit
    num //= 10
print(product)  # Output: 24
if ex== product:
    print("number is palindrome")
else:
    print("number is not palidrome")    
