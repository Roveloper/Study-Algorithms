N = int(input(''))
def plus(n):
  su=0
  for i in range(1,n+1):
    su += i
  return su

for i in range(N):
  OX = input('')
  sum = 0
  step=0

  for k in range(len(OX)):
    if OX[k] == 'O':
      step+=1
    if OX[k] == 'X':
      sum+=plus(step)
      step = 0

  print(sum+plus(step))
