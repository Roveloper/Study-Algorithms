#######
N, M, K = map(int, input().split())
K_col = (K % M)
K_row = (K // M) + 1


def factorial_r(n):
    if n > 1:
        return n * factorial_r(n - 1)
    else:
        return 1


def ncr(n, r):
    res = factorial_r(n) / (factorial_r(r) * factorial_r(n - r))
    return res


if K == 0:
    print(M * N)
else:
    print(int(ncr(K_col, K_row) * ncr(M - K_col + 1, N - K_row + 1)))