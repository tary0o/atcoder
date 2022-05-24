N = int(input())
A = list(map(int,input().split()))
cnt = [0]*(int(1e5))
ans = 0

for a in A:
    cnt[a] += 1

for i in range(1,50000):
    ans += cnt[i]*cnt[int(1e5-i)]
ans += cnt[50000]*(cnt[50000]-1)/2

print(int(ans))