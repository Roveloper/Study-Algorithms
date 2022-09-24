from ast import Pass


N = int(input(""))
#띄어쓰기 없음
# for i in range(0,N):
#     print("*"*((N-1)*2-i) + "*" + "*"*((N-1)*2-i))
#     if i+1 < N:
#         print("*"*(i+1) + " " +"*"*(i+1))
#     else:
#         Pass
    
    
# for i in range(0,N-1):
#     print("*"*(N-i-1) + " " +"*"*(N-i-1))
#     print("*"*((N-1)*2-(N-2-i)) + "*" + "*"*((N-1)*2-(N-2-i)))


#띄어쓰기 있음
for i in range(0,N):
    print("*"*((N-1)*2-i) + "*" + "*"*((N-1)*2-i))
    if i+1 < N:
        print("*"*(i+1) + " " +"*"*(i+1))
    else:
        Pass
    
    
for i in range(0,N-1):
    print("*"*(N-i-1) + " " +"*"*(N-i-1))
    print("*"*((N-1)*2-(N-2-i)) + "*" + "*"*((N-1)*2-(N-2-i)))

