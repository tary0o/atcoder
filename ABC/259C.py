S = input()
T = input()

cntS = []
cntT = []
cnt= 1

for i in range(len(S)):
    if i == len(S)-1:
        cntS.append([S[i],cnt])
        cnt = 1
        break
    if S[i]==S[i+1]:
        cnt += 1
    else:
        cntS.append([S[i],cnt])
        cnt = 1

for i in range(len(T)):
    if i == len(T)-1:
        cntT.append([T[i],cnt])
        break
    if T[i]==T[i+1]:
        cnt += 1
    else:
        cntT.append([T[i],cnt])
        cnt = 1

if len(cntS) != len(cntT):
    print('No')
    exit()

for i in range(len(cntT)):
    if cntS[i][0] == cntT[i][0] and cntS[i][1] <= cntT[i][1]:
        if cntS[i][1] == cntT[i][1]:
            continue
        if cntS[i][1] < cntT[i][1] and cntS[i][1]>=2:
            continue

    print('No')
    exit()
print('Yes')