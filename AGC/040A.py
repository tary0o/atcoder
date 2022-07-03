S = input()
N = len(S)
a = [0]*(N+1)

for i in range(N):
    if S[i] == '<':
        a[i+1] = a[i]+1

for i in range(1,N+1):
    if S[-i] == '>':
        a[-i-1] = max(a[-i]+1,a[-i-1])
print(sum(a))