# 09.04 백준 4673 셀프넘버

numbers = [i for i in range(1, 10001)]
check = []
for n in range(1, 10001):
    for i in str(n):
        n += int(i)
    check.append(n)

numbers_sub_check = [x for x in numbers if x not in check]

for m in range(len(numbers_sub_check)):
    print(numbers_sub_check[m])