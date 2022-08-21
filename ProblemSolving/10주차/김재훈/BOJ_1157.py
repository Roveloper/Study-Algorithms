#단어 공부 문제
# 입력되는 단어에 있는 a ~ z까지의 알파벳 중, 가장 많이 사용된 알파벳을 대문자로 출력
# 가장 많이 사용된 알파벳이 여러개일 경우, ? 출력

S = input()
S = S.upper()

cnt = []
for i in range(65, 91): 
    cnt.append(S.count(chr(i)))


if cnt.count(max(cnt)) == 1:
    print(chr(65 + cnt.index(max(cnt))))
else:
    print('?')