########
N = int(input(""))
sum = 0
for i in range(0,N):
    student, apple = map(int,(input().split()))
    a = apple%student
    sum += a

print(sum)###



# n = int(input(""))
# school = []
# apple =[]
# all = []
# sum = 0
# for i in range(0,n):
#     a, b = input("").split()
    
#     school.append(int(a))
#     apple.append(int(b))
#     all.append(int(b)%int(a))

#     sum = sum + all[i]
# print(sum)

#잘 몰랐던 거 : 초기화 sum= 0, sum = sum + all[i]
#for문 
