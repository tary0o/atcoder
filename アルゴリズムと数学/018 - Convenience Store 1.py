N = int(input())
A = list(map(int,input().split()))
cnt = {100:0,200:0,300:0,400:0}

for a in A:
    cnt[a] += 1

print(cnt[100]*cnt[400]+cnt[200]*cnt[300])