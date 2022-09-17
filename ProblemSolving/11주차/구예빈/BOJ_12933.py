# BOJ_12933


sound = input()
sound_list = list(sound)
quack = ['q', 'u', 'a', 'c', 'k']

duck_number = 0
k_index = 0
tmp = sound_list

while len(tmp) > 4:
    for alphabet in quack:
            for i in sound_list:
                if alphabet == 'k':
                    duck_number += 1
                    k_index = tmp.index('k')
                if i == alphabet:
                    tmp.remove(i)
                    break

print(tmp)




# if k_index < len(sound_list):
#     for i in quack:
#         print(i)
#         # if i == 'k':
#         #     k_index = sound_list.index(i)
#         # sound_list[k_index:].remove(i)
#         sound_list.remove(i)

# for i in sound_list:
#     order = 0
#     if i == quack[order]:
#         order += 1
#         sound_list.remove(i)
#     else:
#         duck_number += 1

print(duck_number)
