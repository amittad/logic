# Print all numbers whose sum of digits is even (1–100). 
# Print numbers whose sum of digits is even (1 to 100)

for num in range(1, 101):
    # Find sum of digits
    sum_of_digits = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum_of_digits += digit
        temp //= 10
    
    # Check if sum is even
    if sum_of_digits % 2 == 0:
        print(num, end=" ")
