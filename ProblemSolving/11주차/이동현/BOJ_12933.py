crying_duck = list(input(''))
cnt = 0
step_lst = ['q', 'u', 'a', 'c', 'k']

def find_quack(sound):
  if len(sound)%5 == 0:
    pass
  else:
    print(-1)
    exit()

def step_quack(cry_idx):
  global cnt
  cryidx = 0
  first = True

  for i in range(cry_idx, len(crying_duck)):
    cd = crying_duck[i]

    if step_lst[cryidx] == cd:
      crying_duck[i] = '-1'
      if cd == 'k':
        if first:
          cnt+=1
          first = False
        cryidx = 0
      else:
        cryidx += 1

find_quack(crying_duck)

for a,b in enumerate(crying_duck):
  if b == 'q':
    step_quack(a)

if crying_duck.count('-1') != len(crying_duck) or cnt == 0:
  print(-1)

elif cnt > 0:
  print(cnt)