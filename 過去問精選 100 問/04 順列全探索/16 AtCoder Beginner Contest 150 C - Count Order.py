import itertools

N = int(input())
P = list(map(int,input().split()))
Q = list(map(int,input().split()))

cnt = 0
for n in itertools.permutations(range(1,N+1)):
    cnt += 1
    chkP = True
    chkQ = True

    for i in range(N):
        if P[i] != n[i]:
            chkP = False
        if Q[i] != n[i]:
            chkQ = False
    
    if chkP:
        a = cnt
    if chkQ:
        b = cnt

print(abs(a-b))