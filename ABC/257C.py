N = int(input())
S = input()
W = list(map(int,input().split()))
l = []
adult = 0
for i in range(N):
    if S[i]=='1':
        adult+=1
    l.append([W[i],S[i]])

sorted_l = sorted(l, reverse=False, key=lambda x:x[0])
print(sorted_l)

ans = adult
bf = sorted_l[0][1]
cnt = 0
for i in range(1,N):
    if bf == sorted_l[i,1]:
        cnt += 1
        continue
    else:
        cnt = 0
        