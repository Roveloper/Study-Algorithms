# codeup_4816
# A 300, B 60, C 10
# 버튼 누른 횟수가 최소


t = int(input())

a_cnt = 0
a_remain = 0
b_cnt = 0
b_remain = 0
c_cnt = 0
c_remain = 0

a_cnt = t // 300
a_remain = t % 300
b_cnt = a_remain // 60
b_remain = a_remain % 60
c_cnt = b_remain // 10
c_remain = b_remain % 10

if c_remain != 0:
    print('-1')
else:
    print(a_cnt, b_cnt, c_cnt)