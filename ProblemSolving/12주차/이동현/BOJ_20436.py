key_lst=[['qwert','@yuiop'],['asdfg','@hjkl'],['zxcv','bnm']]


def position_check(alpa):
  ja=True
  for i in range(len(key_lst)):
    for k in range(len(key_lst[i])):
      row=list(key_lst[i][k])
      if alpa in row:
        idx=row.index(alpa)
        if k == 0:
          ja=True
        elif k == 1:
          ja=False
        return i,k,idx,ja
  

def time_check(lst):
  time = 0
  for i in range(len(lst)-1):
    if i == 0:
      if lst[0] == lst[1]:
        time = 1
      else:
        x=lst[i+1][2]-lst[i][2]
        y=lst[i+1][0]-lst[i][0]
        time+=abs(x)+abs(y)
        time+=1

    elif i >= 1:  
      x=lst[i+1][2]-lst[i][2]
      y=lst[i+1][0]-lst[i][0]
      time+=abs(x)+abs(y)
      time+=1


  return time

ja_lst=[]
mo_lst=[]

start_ja, start_mo = map(str, input('').split())
munja=list(input(''))

j1,j2,j3,tf1 = position_check(start_ja)
m1,m2,m3,tf2 = position_check(start_mo)


ja_lst.append((j1,j2,j3))
mo_lst.append((m1,m2,m3))



for i in munja:
  k1,k2,k3,k4=position_check(i)
  if k4:
    ja_lst.append((k1,k2,k3))
  else:
    mo_lst.append((k1,k2,k3))

mo_time = time_check(mo_lst)
ja_time = time_check(ja_lst)

print(mo_time + ja_time)

# 자음시간
# 모음시간
