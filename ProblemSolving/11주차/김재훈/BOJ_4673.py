def d(n):
    tmp = 0
    for i in str(n):
        tmp += int(i)

    return tmp + n

tmp = set()
for i in range(1, 10001):
    tmp.add(d(i))

for i in range(1, 10001):
    if i in tmp: # set --> O(1), list --> O(N)
        pass
    else:
        print(i)