# BOJ_20436

# 3x6 2차원 키보드 배열을 만든다.
key_list_left = [['q', 'w', 'e', 'r', 't', '@'],
                 ['a', 's', 'd', 'f', 'g', '@'],
                 ['z', 'x', 'c', 'v', '@', '@']]
key_list_right = [['@', 'y', 'u', 'i', 'o', 'p'],
                  ['@', 'h', 'j', 'k', 'l', '@'],
                  ['b', 'n', 'm', '@', '@', '@']]


# x_left, y_left, x_right, y_right, x_goal, y_goal = None, None, None, None, None, None
# trash_left, trash_right, letter_position = None, None, None


# 해당 문자의 좌표를 구하고 좌, 우 구별 해주는 함수를 만든다.
def find_position(char):
    x = 0
    y = 0
    position = "left"
    for i in range(3):
        for j in range(6):
            if key_list_left[i][j] == char:
                x = i
                y = j
                position = 'left'
            elif key_list_right[i][j] == char:
                x = i
                y = j
                position = 'right'
    return x, y, position


# 성우의 왼쪽, 오른쪽 검지의 위치를 입력 받고 좌표를 구한다.
s_left, s_right = input().split()
x_left, y_left, trash_left = find_position(s_left)
x_right, y_right, trash_right = find_position(s_right)


# 출력 하고자 하는 문자를 입력 받는다.
goal = input()
goal_list = list(goal)


# 각 goal 문자의 위치를 파악 하고 현재 위치 와의 차이를 구한 다음 더해준다.
result = 0
cost = 0
for letter in goal_list:
    # 1. 각 문자의 위치를 파악 한다
    x_goal, y_goal, letter_position = find_position(letter)
    # 2. 현재 위치와 차이를 구한다.
    if letter_position == 'left':
        cost = abs(x_goal - x_left) + abs(y_goal - y_left)
        x_left = x_goal
        y_left = y_goal
    else: # 해당 문자가 오른쪽에 있다면
        cost = abs(x_goal - x_right) + abs(y_goal - y_right)
        x_right = x_goal
        y_right = y_goal
    result += 1 + cost
print(result)