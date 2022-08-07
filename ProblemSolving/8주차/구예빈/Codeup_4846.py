# Codeup_4846

school_n = int(input())
count = 0
for i in range(school_n):
    student, apple = map(int, input().split())
    remain = apple % student
    count += remain
print(count)