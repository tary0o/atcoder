import collections,itertools
N,Q = map(int,input().split())
S = input()
P = 0
ans =[]

for _ in range(Q):
    t,x = map(int,input().split())
    if t==1:
        P += x
    if t==2:
        ans.append(S[(x-P)%N-1])

for a in ans:
    print(a)