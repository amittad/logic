def amit():
    for i in range(1,10):
        yield i


for j in amit():
    print(j)    

       