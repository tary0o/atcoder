N = int(input())
L,R = [],[]
for i in range(N):
    Li,Ri = map(int,input().split())
    L.append(Li)
    R.append(Ri)
L.sort()
R.sort()
indexL,indexR = 0,0
cnt = 0
ansL,ansR=[],[]

while True:
    if indexL == N:
        ansR.append(R[-1])
        break
    else:
        if L[indexL] <= R[indexR]:
            if cnt == 0:
                ansL.append(L[indexL])
            cnt += 1
            indexL += 1
        else:
            cnt -= 1
            if cnt == 0:
                ansR.append(R[indexR])
            indexR += 1

for i in range(len(ansL)):
    print(ansL[i],ansR[i])