def draw_star(n):
  stars = [['*']]
  for i in range(2,n+1):
    for star in stars:
      star.insert(0,' ')
      star.insert(0,'*')
      star.extend([' ', '*'])
      
    all_star = ['*'] * (4*i-3)
    blank_star = [' '] * (4*i-3)
    blank_star[0],blank_star[-1]='*','*'

    stars.insert(0,blank_star)
    stars.insert(0,all_star)
    
    all_star = ['*'] * (4*i-3)
    blank_star = [' '] * (4*i-3)
    blank_star[0],blank_star[-1]='*','*'
    stars.append(blank_star)
    stars.append(all_star)
  return stars


N=int(input(''))

star=draw_star(N)
for k in star:
  print(''.join(k))
