# Codeup_4876

# 딱지 그라운드 수 n 입력
n = int(input())

for i in range(n):
    # A가 내는 딱지 입력
    A_list = list(map(int, input().split()))
    A_list.pop(0)
    A_list.sort()
    # print(A_list)
    # B가 내는 딱지 입력
    B_list = list(map(int, input().split()))
    B_list.pop(0)
    B_list.sort()
    # print(B_list)

    # A, B의 각각의 딱지를 비교한다.
    A_star_number = A_list.count(4)
    A_circle_number = A_list.count(3)
    A_square_number = A_list.count(2)
    A_triangle_number = A_list.count(1)

    B_star_number = B_list.count(4)
    B_circle_number = B_list.count(3)
    B_square_number = B_list.count(2)
    B_triangle_number = B_list.count(1)
    if A_star_number > B_star_number:
        print('A')
    elif A_star_number < B_star_number:
        print('B')
    else:
        if A_circle_number > B_circle_number:
            print('A')
        elif A_circle_number < B_circle_number:
            print('B')
        else:
            if A_square_number > B_square_number:
                print('A')
            elif A_square_number < B_square_number:
                print('B')
            else:
                if A_triangle_number > B_triangle_number:
                    print('A')
                elif A_triangle_number < B_triangle_number:
                    print('B')
                else:
                    print('D')



