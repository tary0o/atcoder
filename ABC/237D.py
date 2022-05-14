N = int(input())
S = input()
L=[]
R=[]

for i in range(N):
    if S[i] == 'L':
        R.append(i)
    if S[i] == 'R':
        L.append(i)

A = L + [N] + R[::-1]
print(*A)