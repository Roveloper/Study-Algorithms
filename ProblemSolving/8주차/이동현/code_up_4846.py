N=int(input(''))
count = 0
for i in range(N):
  A,B = map(int,input('').split())
  count+=B%A

print(count)
