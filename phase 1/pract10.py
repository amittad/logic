num=int(input("enter  a number=")) #234
product=1
add=0
store=[]
while num>0:
  ld=num % 10
  store.append(ld)
  print(f"last value===={ld}")
  product *= ld
  print(f"product of value===={product}")
  num //= 10
  print(f"remaining digits===={num}")
  add+=ld
print(product)
print(store)



