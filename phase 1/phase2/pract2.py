num = 234
product = 0
while num > 0:
    digit = num % 10
    product=product*10+digit
    num //= 10
print(product)  #