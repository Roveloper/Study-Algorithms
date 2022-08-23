eight = input('')
lst = []
for i in eight:
  lst.append(i)
lst.reverse()
sum=0
for k in range(len(lst)):
  sum+=int(lst[k]) * 8**k
two=[]
while sum > 0:
  j+=1
  if sum // 2**j == 0:
    sum-= 2**(j-1)
    two.append(j-1)
    j=0

ans = [0 for i in range(max(two)+1)]
for u in two:
  ans[int(u)]=1

ans.reverse()
for y in ans:
  print(y, end='')


O=int(input(), 8)
num_2 = format(O,'b')
print(num_2)
