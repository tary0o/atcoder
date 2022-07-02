N = int(input())
A = list(map(int,input().split()))
state = [0]*4
P = 0

for a in A:
    if state[3]:
        P += 1
        state[3] = 0
    if state[2]:
        if a>1:
            P += 1
        else:
            state[2+a] = 1
        state[2] = 0
    if state[1]:
        if a>2:
            P += 1
        else:
            state[1+a] = 1
        state[1] = 0
    if a==4:
        P += 1
    else:
        state[a] = 1
print(P)