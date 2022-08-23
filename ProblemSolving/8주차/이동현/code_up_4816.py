N=int(input())
A=300
B=60
C=10
count_A = N//300

NB = N - count_A*300
count_B = NB//60

NC = NB - count_B*60

count_C = NC//10

ND = NC-count_C*10

if ND !=0:
  print('-1')

else:
  print(f'{count_A} {count_B} {count_C}')
