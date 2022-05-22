N = int(input())

sosuu = {i for i in range(2,N+1)}

for i in range(2,N+1):
    if i in sosuu:
        tmp = i
        while tmp < N:
            tmp += i
            sosuu.discard(tmp)

for ans in sosuu:
    print(ans)