N = int(input())
d = sorted( [int(input()) for i in range(N)] )
count = 1
for i in range(N-1):
    if d[i] < d[i+1]:
        count += 1

print(count)