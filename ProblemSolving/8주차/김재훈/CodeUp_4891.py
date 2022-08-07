# 행복감과 학생들의 성적 차이 관계 확인하기로 함
# 이전 성적과의 시험 점수 차이 변화를 확인

# N명 학생들의 점수가 주어졌을 때, 가장 높은 점수와 가장 낮은 점수 차이를 구하는 프로그램 작성

N = int(input())

score_lst = list(map(int, input().split()))

print(max(score_lst) - min(score_lst))