n=int(input(''))
for i in range(n):
  num=int(input(''))
  k=list(map(int,input('').split()))
  print(min(k), max(k))