#N은 딱지놀이의 총 라운드 수
#a : A가 내는 딱지에 나온 그림의 총 개수 
#b : B가 내는 딱지에 나온 그림의 총 개수
#4 > 3 > 2 > 1순 높은 숫자가 많으면 이기는 게임

N = int(input())
for i in range(0,N):
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))

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






























# def cards(card_list): 
#     cards_count = [0, 0, 0, 0]
#     ls = list(card_list)
#     card_number = ls.pop(0)
#     for i in range(card_number):
#         cards_count[ls[i] - 1] += 1
#     return cards_count.reverse()  


# def shobu(A_cards, B_cards):
#     for i in range(4):
#         if A_cards[i] > B_cards[i]:  
#             return 1
#         elif A_cards[i] < B_cards[i]:  
#             return -1
#     return 0  


# history = []

# N = int(input())

# for i in range(N):
#     A_cards = cards(map(int, input().split()))
#     B_cards = cards(map(int, input().split()))
#     history.append(shobu(A_cards, B_cards))

# for his in history:
#     if his == 1:
#         print('A')
#     elif his == -1:
#         print('B')
#     else:
#         print('D')