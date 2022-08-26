All_person = list(range(1,31))
attendance = []
for i in range(28):   #for문 직관적
    student = int(input())
    attendance.append(student)

absentee = list(set(All_person)-set(attendance))

#set을 쓰면 중복 허용 x, 순서 무작위
    
for j in sorted(absentee):
    print(j)