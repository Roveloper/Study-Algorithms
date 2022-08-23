word = input('')
alpa = list(range(97,123))
for i in alpa:
  index = word.find(chr(i))
  print(index, end = ' ')
