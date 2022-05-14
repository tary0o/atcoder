N,K = map(int,input().split())
S = [input() for _ in range(N)]
ans = 0

for i in range(2**(N)):
    bit = [ i>>j&1 for j in range(N) ]
    anscount = 0
    check = list()
    checkS = set()
    for j in range(N):
        if bit[j] == 1:
            check.append(S[j])
            checkS |= set(S[j])

    for s in checkS:
        count = 0
        for j in range(len(check)):
            if s in check[j]:
                count += 1
        if count == K:
            anscount += 1
    
    ans = max(ans,anscount)
print(ans)