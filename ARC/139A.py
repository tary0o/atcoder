N = int(input())
T = list(map(int,input().split()))

ans = [1] + [0]*T[0]

for i in range(1,N):
    tmp = [1]*len(ans-T[i])
