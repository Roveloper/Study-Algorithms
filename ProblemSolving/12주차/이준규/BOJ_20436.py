#      이동시간 누른시간 총시간
# z        0       1       1
# o        0       1       2
# a        1       1       4
# c        3       1       8
left = ['qwert','asdfg','zxcv']
right = ['*yuiop','*hjkl','bnm']
sl, sr = map(str,input().split())
for i in range(3):
    if sl in left[i]:
        ly = i
        lx = left[i].index(sl)
        # print(lx, ly)
    if sr in right[i]:
        ry = i
        rx = right[i].index(sr)

word = input()
res = 0
new_lx, new_ly, new_rx, new_ry = 0, 0, 0, 0

for j in range(len(word)):
    check = word[j]
    for k in range(3):
        if check in left[k]:
            temp_lx = left[k].index(check)
            temp_ly = k
            dis = abs(temp_lx - lx) + abs(temp_ly - ly)
            lx = temp_lx
            ly = temp_ly
            res += 1+dis
        if check in right[k]:
            temp_rx = right[k].index(check)
            temp_ry = k
            dis = abs(temp_rx - rx) + abs(temp_ry - ry)
            rx = temp_rx
            ry = temp_ry
            res += 1 + dis
print(res)

