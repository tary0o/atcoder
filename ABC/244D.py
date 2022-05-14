S = input().split()
T = input().split()

if S == T:
    print('Yes')
elif S[0] != T[0] and S[1] != T[1] and S[2] != T[2]:
    print('Yes')
else:
    print('No')