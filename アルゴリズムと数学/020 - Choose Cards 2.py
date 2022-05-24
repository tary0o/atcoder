N = int(input())
A = list(map(int,input().split()))
cnt = 0

for a in range(N-4):
    for b in range(a+1,N-3):
        for c in range(b+1,N-2):
            for d in range(c+1,N-1):
                    for e in range(d+1,N):
                        if A[a]+A[b]+A[c]+A[d]+A[e] == 1000:
                            cnt += 1
print(cnt)