N=int(input(''))
lst=[]
score=map(int,input('').split())
for i in score:
  lst.append(i)

k=max(lst)-min(lst)

print(k)
