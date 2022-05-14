from collections import deque

Q = int(input())
tutu = deque()
ans = []

for _ in range(Q):
    ixc = list(map(int,input().split()))

    if ixc[0] == 1:
        x,c = ixc[1],ixc[2]
        tutu.append([x,c])
    
    if ixc[0] == 2:
        tempans = 0
        c = ixc[1]

        while c > 0:
            tutux,tutuc = tutu[0]

            if tutuc <= c:
                c -= tutuc
                tempans += tutux*tutuc
                tutu.popleft()
            else:
                tempans += tutux*c
                tutu[0][1] -= c
                c = 0
        ans.append(tempans)

for a in ans:
    print(a)