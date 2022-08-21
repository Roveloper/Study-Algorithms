# 알파벳 찾기
# 알파벳 소문자로만 이루어진 단어 S가 입력됨
# 전체 알파벳에 대해, 해당 알파벳이 포함되어있으면, 포함되어있는 위치를 출력
# 포함되어있지 않다면 -1을 출력하는 프로그램 작성

input_str = input()

for i in range(97, 123):
    print(input_str.find(chr(i)), end=' ')
