N,M = map(int,input().split())
S = list(map(str,input().split()))
T = list(map(str,input().split()))[::-1]

for i in range(N):
    result = 'No'

    if S[i] == T[M-1]:
        result = 'Yes'
        M -= 1

    print(result)

"""
T = set(input().split())
for i in range(N):
    result = 'No'
    if S[i] in T:
        result = 'Yes'
    print(result)
"""