N,K = map(int,input().split())
a = list(map(int,input().split()))
b = sorted(a)

for i in range(K):
    ak,bk =[],[]
    j = i
    while j < N:
        ak.append(a[j])
        bk.append(b[j])
        j += K
    ak.sort()

    for i in range(len(ak)):
        if ak[i] != bk[i]:
            print('No')
            exit()
print('Yes')