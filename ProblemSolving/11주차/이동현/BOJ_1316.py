N = int(input(''))
lst=[]
for _ in range(N):
    word = input('')
    lst.append(word)
    for i in range(len(word)-1):
      if word[i] == word[i+1]:
        pass
      elif word[i] in word[i+1:]:
        N -= 1
        break
        
print(N)