Isreap=int(input(''))
if Isreap % 4 ==0:
  if Isreap % 100 == 0 and Isreap % 400 != 0:
    print('0')
  else: print('1')
  
else:
  print('0')
