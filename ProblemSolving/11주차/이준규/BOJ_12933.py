# 09.04 백준 12933 오리
duck_sounds = input()
duck = ['q', 'u', 'a', 'c', 'k']
check = [0 for _ in range(len(duck_sounds))]
x = 0
res = 0
if len(duck_sounds) % 5 != 0:
    print("-1")
elif duck_sounds[0] != 'q' or duck_sounds[-1] != 'k':
    print("-1")
else:
    for i in range(len(duck_sounds)):

        run = True
        if duck_sounds[i] == 'q' and check[i] != 1:
            for j in range(len(duck_sounds)):
                if check[j] != 1 and duck[x] == duck_sounds[j]:
                    check[j] = 1
                    # print(check)
                    if duck_sounds[j] == 'k':
                        if run:
                            res += 1

                            run = False
                        # res += 1
                        x = 0
                        continue
                    else:
                        x += 1

    if 0 in check:
        print(-1)
    else:
        print(res)
