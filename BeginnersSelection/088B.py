N = int(input())
a = list( map(int,input().split()) )
dif = 0

a.sort(reverse=True)
for i in range(len(a)):
    dif += (-1)**i * a[i]

print(dif)