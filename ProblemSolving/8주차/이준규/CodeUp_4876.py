# 08.07

# 별 > 동그라미 > 네모 > 세모 -> 다 같으면 무승부
# 별 : 4, 동그라미 : 3, 네모 : 2, 세모 : 1
N = int(input())
for _ in range(N):
    A = list(map(int,input().split()))
    A.pop(0)
    B = list(map(int,input().split()))
    B.pop(0)
    if A.count(4) > B.count(4):
        print("A")
    elif A.count(4) < B.count(4):
        print("B")
    else:
        if A.count(3) > B.count(3):
            print("A")
        elif A.count(3) < B.count(3):
            print("B")
        else:
            if A.count(2) > B.count(2):
                print("A")
            elif A.count(2) < B.count(2):
                print("B")
            else:
                if A.count(1) > B.count(1):
                    print("A")
                elif A.count(1) < B.count(1):
                    print("B")
                else:
                    print("D")