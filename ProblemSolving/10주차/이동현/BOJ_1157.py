from collections import Counter
Word = input('')
wording = Word.lower()
lst=[]
for i in wording:
  lst.append(i)

count_item = Counter(lst)
if len(set(lst))==1:
  max_item = count_item.most_common(n=1)
  print(max_item[0][0].upper())
else:
  max_item2 = count_item.most_common(n=2)
  if max_item2[0][1]==max_item2[1][1]:
    print('?')
  else:
    print(max_item2[0][0].upper())
