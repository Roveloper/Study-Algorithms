N = int(input())
L = 4 * N - 3# 2N-2 + 1 + 2N-2

if N == 1:
    print("*")
else:
    store = [[]] * (2 * (N - 1))
    for i in range(N-1):
        l1 = "* "*i + "*"*(L-4*i) + " *"*i
        l2 = "* "*(i+1) + " "*(L-4*(i+1)) + " *"*(i+1)
        store[2*i] = l1
        store[2*i+1] = l2
        print(l1)
        print(l2)
    print("* "*(2*N-1))
    # print(store)

    for j in range(len(store)-1,-1,-1):
        print(store[j])
