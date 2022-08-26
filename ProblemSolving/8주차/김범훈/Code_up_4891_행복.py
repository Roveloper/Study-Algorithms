# Student_number = int(input())
# student = list(map(int,input().split()))
##########
# max = 0
# min = 1000
# for i in student:
#     if i > max:
#         max = i

# for i in student:
#     if i < min:
#         min = i

# print(max - min)

##########################다른 풀이#########################
# Student_number = int(input(" "))

# Score = list(map(int,input("").split()))

# print(max(Score)-min(Score))



#######map 주의사항##############
# Score, student = map(int,input("").split())

# print(Score-student)
     



#split()-> string 자료형으로 list 형식으로 변환
#map함수로 string자료형을 int형으로 바꾸어준다. input()함수와 함께 사용된다.


# max = 0 #초기화하기!!!!!!!!!!!!!!!!!!!!!!
# for i in Score:
#     if i > max:
#         max = i
    
# print(max)