# ZOAC2 문제
# 한글 자음은 왼손, 한글 모음은 오른손으로 입력

def find_idx(cha):
    # 이거는 특정 문자의 위치를 찾는 함수입니다.
    keyboard_lst = [list('qwertyuiop'), list('asdfghjkl'), list('zxcvbnm')]
    
    for i, keys in enumerate(keyboard_lst):
        if cha in keys: # 우선 1행, 2행, 3행 중에 하나를 찾고
            tmp_r = i # 행
            tmp_c = keys.index(cha) # 해당 행에 몇번째 열에 있는 지 확인했습니다.
            
    return tmp_r, tmp_c # 행, 열 순서대로 찾아줍니다.
    # qwertyuiop --> 1행, w --> 1행 2열 --> [0, 1] 로 결과가 나옵니다.
    # asdfghjkl --> 2행
    # zxcvbnm --> 3행
left_hand_keys = list('qwertasdfgzxcv') # 왼손으로 누르는 키
right_hand_keys = list('yuiophjklbnm') # 오른손으로 누르는 키

lh, rh = input().split() # 왼손 시작 위치, 오른손 시작 위치
l_idx = find_idx(lh) # 왼손 행렬 찾기
r_idx = find_idx(rh) # 오른손 행렬 찾기

result_time = 0 # 전체 시간 초기화

word = input() # 입력해야하는 단어 입력 받기

for i in word: # 각 단어 살피기
    tmp_idx = find_idx(i) # 해당 문자의 행렬 위치 찾기
    if i in left_hand_keys: # 해당 문자가 왼쪽에 있는지 오른쪽에 있는지 확인
        result_time += (abs(l_idx[0] - tmp_idx[0]) + abs(l_idx[1] - tmp_idx[1]))
        # 기존에 왼쪽 손가락 위치에서 이동하는 시간을 계산해서 더해줍니다.
        l_idx = tmp_idx
        # 그리고 손가락 위치를 새로운 문자의 위치로 변경
        result_time += 1
        # 누르는 시간 1초 추가
    elif i in right_hand_keys: # 해당 문자가 왼쪽에 있는지 오른쪽에 있는지 확인
        # 위와 같습니다.
        result_time += (abs(r_idx[0] - tmp_idx[0]) + abs(r_idx[1] - tmp_idx[1]))
        r_idx = tmp_idx
        result_time += 1
    else:
        # 혹시 몰라서, 왼손 오른손에 다 없는 경우 확인용으로 추가
        print('뭔가 잘못됨')

print(result_time) # 결과 출력

# 나레이션 고맙습니다 :)
# 오늘은 여기까지 :), 그럼 안녕 :)
# 다음주에는 밖에 나갈게요, 24시간 카페를 찾아야겠네요
