N,M = map(int,input().split())
x = []
y = []

for i in range(M):
    xi,yi = map(int,input().split())
    x.append(xi)
    y.append(yi)

ans = 1
for test in range (2**N):
    cnt = 0
    for i in range(N):
        if i == N-1:
            if ((test>>i) & 1):
                cnt += 1
        elif ((test>>i) & 1):
            cnt += 1
            for j in range(i+1,N):
                if ((test>>j) & 1):
                    chk = False
                    for k in range(M):
                        if x[k] == i+1 and y[k] == j+1:
                            chk = True
                            
                    if not chk:
                        break
            else:
                continue
            break
    else:
        if ans < cnt:
            ans = cnt

print(ans)