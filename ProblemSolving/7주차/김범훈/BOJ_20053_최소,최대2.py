T = int(input())
for i in range(0,T):
    N = int(input())
    L = list(map(int, input().split()))
    # L = [int(x) for x in input().split()]
    print(min(L),max(L))



n = input().split()
m = list(map(int,input().split()))
print("m",m)    #결과 값 [20,30,40]
print("n",n)    #결과 값 ['20','30','40']
print(type(m))
print(type(n))