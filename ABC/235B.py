N = int(input())
H = list( map(int,input().split()) )
hight = H[0]

for i in range(1,N):
    if hight < H[i]:
        hight = H[i]
    else:
        break

print(hight)