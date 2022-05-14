S = list(input())
a,b = map(int,input().split())

output = S[:]
output[a-1] = S[b-1]
output[b-1] = S[a-1]

print(''.join(output))