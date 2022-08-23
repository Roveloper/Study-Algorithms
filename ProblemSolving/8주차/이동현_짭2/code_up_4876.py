N=int(input(''))
for _ in range(N):
  A = list(map(int, input().split()))
  B = list(map(int, input().split()))

  A.pop(0)
  B.pop(0)
  A_star=A.count(4)
  B_star=B.count(4)
  A_circle=A.count(3)
  B_circle=B.count(3)
  A_squr=A.count(2)
  B_squr=B.count(2)
  A_tri=A.count(1)
  B_tri=B.count(1)
  if A_star > B_star:
    print('A')
  elif A_star < B_star:
    print('B')
  else:
    if A_circle > B_circle:
      print('A')
    elif A_circle < B_circle:
      print('B')
    else:
      if A_squr > B_squr:
        print('A')
      elif A_squr < B_squr:
        print('B')
      else:
        if A_tri > B_tri:
          print('A')
        elif A_tri < B_tri:
          print('B')
        else:print('D')
