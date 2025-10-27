

for i in range(1,500):       # Loop through numbers 1 to 499
    temp = i                 # Store the number in a temporary variable
    product = 0              # Initialize variable to store reversed number

    while temp > 0:          # Reverse the number
        digit = temp % 10        # Get last digit
        product = product*10 + digit  # Add digit to reversed number
        temp = temp // 10           # Remove last digit

    if i == product:          # Compare original and reversed
        print(i)              # If same → palindrome
