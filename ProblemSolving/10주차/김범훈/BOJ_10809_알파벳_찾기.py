S = input("")

word = "abcdefghijklmnopqrstuvwxyz"

for i in word:
    if i in S:
        print(S.index(i),end=' ')
    else:
        print(-1, end=' ')

     


