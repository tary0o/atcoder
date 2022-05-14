N,A,B = map(int,input().split())

ans = [ ['.']*(B*N) for _ in range(A*N)]


for i in range(N):
    if i%2 == 0:
        for y in range(i*A,(i+1)*A):
            xcount = 0
            color = 1
            for x in range(B*N):
                if xcount == B:
                    color *= -1
                    xcount = 0
                if color == 1:
                    ans[y][x] = '.'
                else:
                    ans[y][x] = '#'
                xcount += 1
    else:
        for y in range(i*A,(i+1)*A):
            color = 1
            xcount = 0
            for x in range(B*N):
                if xcount == B:
                    color *= -1
                    xcount = 0

                if color == 1:
                    ans[y][x] = '#'
                else:
                    ans[y][x] = '.'
                xcount += 1

for y in range(A*N):
    for x in range (B*N):
        print(ans[y][x],end='')
    print()