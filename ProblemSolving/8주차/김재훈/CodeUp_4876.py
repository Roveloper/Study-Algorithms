# 별, 동그라미, 네모, 세모 중 하나가 표시된 딱지
 
# 딱지의 강력함은 다음 규칙
# 별의 개수가 다르다면, 별이 많은게 이김
# 별의 개수가 같다면, 동그라미가 많은게 이김
# 별, 동그라미도 같다면, 네모가 많은게 이김
# 별, 동그라미, 네모도 같다면, 세모가 많은게 이김
# 별, 동그라미, 네모, 세모가 같다면 무승부입니다.

N = int(input())

for _ in range(N):
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.pop(0)
    B.pop(0)

    A_star_cnt = A.count(4)
    B_star_cnt = B.count(4)
    A_circle_cnt = A.count(3)
    B_circle_cnt = B.count(3)
    A_square_cnt = A.count(2)
    B_square_cnt = B.count(2)
    A_triangle_cnt = A.count(1)
    B_triangle_cnt = B.count(1)

    if A_star_cnt > B_star_cnt:
        print("A")
        
    elif A_star_cnt < B_star_cnt:
        print("B")
    
    elif A_circle_cnt > B_circle_cnt:
        print("A")
    
    elif A_circle_cnt < B_circle_cnt:
        print("B")
    
    elif A_square_cnt > B_square_cnt:
        print("A")
    
    elif A_square_cnt < B_square_cnt:
        print("B")

    elif A_triangle_cnt > B_triangle_cnt:
        print("A")
    
    elif A_triangle_cnt < B_triangle_cnt:
        print("B")

    else:
        print("D")

