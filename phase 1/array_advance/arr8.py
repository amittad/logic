arr = [10, 2, 3, 4, 51, 6, 33, 1, 22, 67]
prime_count = 0

for i in arr:
    if i > 1:  # prime numbers are greater than 1
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                break
        else:
            prime_count += 1

print("Count of prime numbers:", prime_count)
