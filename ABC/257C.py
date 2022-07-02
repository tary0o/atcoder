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

tmpans = adult
ans = adult
cnt = [0,0]
for i in range(1,N+1):
    if i != N:
        if sorted_l[i-1][0] == sorted_l[i][0]:
            cnt[0] += 1
            if sorted_l[i-1][1]=='0':
                cnt[1] += 1
        else:
            if cnt[0]==0:
                if sorted_l[i-1][1]=='0':
                    tmpans += 1
                else:
                    tmpans -= 1
            else:
                cnt[0] += 1
                if sorted_l[i-1][1]=='0':
                    cnt[1] += 1
                tmpans += (-cnt[0]+2*cnt[1])
                cnt = [0,0]
    else:
        if cnt[0] == 0:
            if sorted_l[i-1][1]=='0':
                tmpans += 1
            else:
                tmpans -= 1
        else:
            if sorted_l[i-1][1]=='0':
                cnt[1] += 1
            cnt[0] += 1
            tmpans += (-cnt[0]+2*cnt[1])
    ans = max(ans,tmpans)

print(ans)
        