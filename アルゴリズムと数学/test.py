N,A,B = map(int,input().split())

ans = [ ['.'*(B*N)] for _ in range(A*N)]
white = [ ['.'*(B)] for _ in range(A)]
black =  [ ['#'*(B)] for _ in range(A)]

for i in range(1,N+1):
    if i%2 == 1:
        print(0)
        ans[(i-1)*A:i*A][(i-1)*B:i*B] = white
    else:
        print(1)
        ans[(i-1)*A:i*A][(i-1)*B:i*B] = black      

for i in range(A*N):
    print(*ans[i][:])