# Take input from user
s = input("Enter a string: ")

# Check if string length is at least 2
if len(s) >= 2:
    new_str = s[:2] + s[-2:]
else:
    new_str = "String too short!"

print("New string:", new_str)
