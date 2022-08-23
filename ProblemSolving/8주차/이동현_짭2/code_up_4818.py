def factorial(N):
  if N==0:
    return 1
  else:
    return N*factorial(N-1)

N,M,K = map(int,input('').split())
if K == 0:
  nCr_ori=factorial(N+M-2)/((factorial(N-1))*(factorial(M-1)))
  print(int(nCr_ori))
else:
  down=K//M
  right=K%M
  if right == 0 :
    right=M-1
    down-=1
    right_res=0
  else:
    right=right-1
    right_res=M-right-1

  nCr=factorial(down+right)/((factorial(down))*(factorial(right)))

  down_res=N-down-1

  nCr_res=factorial(down_res+right_res)/((factorial(down_res))*(factorial(right_res)))
  print(int(nCr_res*nCr))
