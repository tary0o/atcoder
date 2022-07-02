N = int(input())
A = [input() for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(N):
        tmp1 = []
        tmp2 = []
        tmp3 = []
        tmp4 = []
        for k in range(N):
            tmp1.append(int(A[(i+k)%N][j]))
            tmp2.append(int(A[(i-k)%N][j]))
            tmp3.append(int(A[i][(j+k)%N]))
            tmp4.append(int(A[i][(j-k)%N]))
        tmp1 = int("".join(map(str, tmp1)))
        tmp2 = int("".join(map(str, tmp2)))
        tmp3 = int("".join(map(str, tmp3)))
        tmp4 = int("".join(map(str, tmp4)))
        ans = max(ans,tmp1,tmp2,tmp3,tmp4)

        tmp1 = []
        tmp2 = []
        tmp3 = []
        tmp4 = []
        for k in range(N):
            tmp1.append(int(A[(i+k)%N][(j+k)%N]))
            tmp2.append(int(A[(i-k)%N][(j-k)%N]))
            tmp3.append(int(A[(i+k)%N][(j-k)%N]))
            tmp4.append(int(A[(i-k)%N][(j+k)%N]))
        tmp1 = int("".join(map(str, tmp1)))
        tmp2 = int("".join(map(str, tmp2)))
        tmp3 = int("".join(map(str, tmp3)))
        tmp4 = int("".join(map(str, tmp4)))
        ans = max(ans,tmp1,tmp2,tmp3,tmp4)

print(ans)