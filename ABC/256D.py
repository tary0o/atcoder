import sys
input = sys.stdin.readline
 
N = int(input())
S = [0]*(2*10**5+1)
 
for i in range(N):
    L,R = map(int,input().split())
    S[L:R] = [1]*(R-L)
 
l = 0
ans = []
ansl,ansr = [],[]
for i in range(1,2*10**5+1):
    if S[i]==1 and l==0:
        ansl = i
        l = 1
    if S[i]==0 and l==1:
        ansr = i
        l = 0
        ans.append([ansl,ansr])
 
for a in ans:
    print(a[0],a[1])