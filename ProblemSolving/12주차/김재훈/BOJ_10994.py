# 별찍기 19
# 가로 줄 수  --> (N - 1) * 4 + 1
# 세로 줄 수  -->                  

# def draw_stars(N):
#     tmp_stars = []
#     for i in range(0, 4 * N - 3):
#         if i == 0 or i == (4 * N - 4):
#             tmp_stars.append(['*'] * (4 * N - 3))
#         else:
#             tmp_lst = [' '] * (4 * N - 3)
#             tmp_lst[0] = '*'
#             tmp_lst[4 * N - 4] = '*'
#             tmp_stars.append(tmp_lst)

#     return tmp_stars

# def add_stars(N):
#     stars = draw_stars(N)
#     N -= 1
#     while N != 0:
#         tmp_stars = draw_stars(N)
#         for i in tmp_stars:
#             stars[2 * N : len(stars) - (2 * N) + 1] = i
#         for i in range(2 * N, len(stars) - (2 * N) + 1):
#             stars[2 * N : len(stars) - (2 * N) + 1] = tmp_stars
            
            
def draw_stars(N):
    stars = [['*']] # 시작 별 (1일 때 * 한개만 있는 거요)
    for i in range(2, N + 1):
        for star in stars:
            star.insert(0, ' ') # 왼쪽에 빈칸
            star.insert(0, '*') # 왼쪽에 * 
            # 여기는 왼쪽에 추가
            # 위에 두줄 진행하면 ['*', ' ', '*']이 됩니다. 기존에 있던 거에 왼쪽에 '*' ' '을 추가
            star.extend([' ', '*'])
            # 여기는 오른쪽에 추가
            # 여기는 반대로 오른쪽에 ' ', '*'을 추가하는 부분입니다.
        # 여기 for문을 돌면, 기존에 있던 별들의 왼쪽 오른쪽에 '*' ' ', ' ', '*'을 추가한 것
        
        # * --> * * * 이렇게 됩니다.
        # 여기서부터는 위아래를 채우는 부분
        all_star = ['*'] * (4 * i - 3)
        # all_star = '*****'
        blank_star = [' '] * (4 * i - 3)
        blank_star[0] = '*'
        blank_star[-1] = '*'
        # blank_star = '*   *'
        stars.insert(0, blank_star)
        stars.insert(0, all_star)
        # 위에 추가
        # 여기 위에 두줄은 all_star를 앞에, blank_star를 뒤에 추가
        all_star = ['*'] * (4 * i - 3)
        blank_star = [' '] * (4 * i - 3)
        blank_star[0] = '*'
        blank_star[-1] = '*'
        stars.append(blank_star)
        stars.append(all_star)
        # 아래에 추가
        # 여기 밑에 두줄은 맨 아래쪽에 두줄을 추가
    return stars
        
        
            

N = int(input())

stars = draw_stars(N)
for i in stars:
    print(''.join(i))

'''간단히 말해서, N이 늘어나면 왼쪽 오른쪽에 *이랑 빈칸이 추가되고
그 다음에 위랑 아래에 *로만 이루어진 줄 하나랑 왼쪽오른쪽에 *만 있는 줄이 추가됩니다

중요한건 좌우 대칭이고, 상하 대칭이라 추가하는 순서만 반대로 하면 똑같습니다.
        *****
* -->   *   *
        * * *
        *   *
        *****
구글링은 밖을 먼저 그리고 안에 별 그리기
제가 한건 별 하나로 시작해서, 상하좌우에 추가하는 구조
'''
