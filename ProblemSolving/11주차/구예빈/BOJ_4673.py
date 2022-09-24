# BOJ_4673

sum_list = []
# 1 - 10000까지를 생성자로 하여 d(n) 리스트 sum_list를 구해준다.
for i in range(1, 10001):
    # i의 자릿수
    digit_sum = i % 10
    tmp = i // 10
    while tmp != 0:
        digit_sum += tmp % 10
        tmp = tmp // 10
    sum_list.append(i + digit_sum)
print(sum_list)

# 1 - 10000까지 sum_list에 없는 수, self_number를 출력해준다.
for self_number in range(1, 10001):
    if sum_list.count(self_number) == 0:
        print(self_number)


