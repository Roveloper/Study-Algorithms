lst=[i for i in range(1,10001)]
for i in range(1,10000):
  init=str(i)
  sum = 0
  for k in init:
    sum+=int(k)
  new_number=sum+i
  if new_number in lst:
    (lst.remove(new_number))
for k in lst:
  print(k)