N,L,W = map(int,input().split())
a = list(map(int,input().split()))
a.append(L)

count = 0
state = 0

for i in a:
    if i > state:
        count += -(-(i-state)//W)
    state = i+W

print(count)