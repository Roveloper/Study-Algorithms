people, room_per = map(int,input('').split())

boy_lst=[]
girl_lst=[]
for i in range(people):
  sex, grade = map(int,input('').split())
  if sex == 0:
    girl_lst.append(grade)
  else:
    boy_lst.append(grade)
# print(boy_lst)
# print(girl_lst)

boy_count=0
for j in range(1,7):
  if boy_lst.count(j)%(room_per)==0:
    boy_count+=int(boy_lst.count(j)//(room_per))
  else:
    boy_count+=int(boy_lst.count(j)//(room_per) + 1)
    
girl_count=0
for j in range(1,7):
  if girl_lst.count(j)%(room_per)==0:
    girl_count+=int(girl_lst.count(j)//(room_per))
  else:
    girl_count+=int(girl_lst.count(j)//(room_per) + 1)
print(girl_count+boy_count)
