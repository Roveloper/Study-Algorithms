#학생들 점수의 최대 최솟 값 차이 구하기
#N : 학생수 , 리스트 정렬 : .sort() , .reverse() ..
N = int(input())
score = list(map(int, input().split()))
Max = max(score)
Min = min(score)
diff = Max-Min
print(diff)
