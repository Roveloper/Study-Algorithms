cry = list(input())

if len(cry) % 5 != 0:
    print(-1)
    exit()
    
correct_cry = 'quack'
cnt = 0

def find_duck(i): # quqacukqauackck --> -1 -1 q -1 -1 u -1 -1 a -1 -1 -1 -1 c k --> -1 
     
    global cnt
    correct_cry_idx = 0
    first = True
    
    for idx in range(i, len(cry)):
        ch = cry[idx]
        
        if correct_cry[correct_cry_idx] == ch:
            cry[idx] = -1
            if ch == 'k':
                if first:
                    cnt += 1
                    first = False
                correct_cry_idx = 0
            else:
                correct_cry_idx += 1

for idx, ch in enumerate(cry):
    if ch == 'q':
        find_duck(idx)
        
if (cry.count(-1) != len(cry)) or cnt == 0:
    print(-1)
elif cnt > 0:
    print(cnt)