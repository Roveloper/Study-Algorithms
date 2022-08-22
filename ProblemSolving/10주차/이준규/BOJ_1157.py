S = input()
big_S = S.upper()
alp_list = list(set(big_S))
cnt_list = [big_S.count(i) for i in alp_list]

res = cnt_list.count(max(cnt_list))
# print(big_S,alp_list, cnt_list, res)
if res == 1:
    print(alp_list[cnt_list.index(max(cnt_list))])
else:
    print("?")

