#Check if all elements in an array are unique.
 


arr = [1, 2, 3, 4,5]
arr2 = []
unique = True

for i in arr:
    if i in arr2:  # check if element already exists
        print("Not unique")
        unique = False
        break
    else:
        arr2.append(i)

if unique:
    print("All elements are unique")

