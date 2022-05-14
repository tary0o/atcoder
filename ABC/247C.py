import sys
sys.setrecursionlimit(100)

N = int(input())

def f(N):
    if N == 1:
        S = [1]
    else:
        S = f(N-1)
        S.append(N)
        S += f(N-1)
    
    return S

print(*f(N))