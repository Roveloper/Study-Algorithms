number = set(range(1,10001))
con_number = set()

for i in range(1,10001):
    for j in str(i):
        i +=int(j)
    con_number.add(i)
self_num = sorted(number -con_number)
for i in self_num:
    print(i)