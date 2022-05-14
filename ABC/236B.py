N = int(input())
A = list(map(int,input().split()))
count = [0]*(N+1)

for i in A:
    count[i] += 1

for i in range(1,N+1):
    if count[i] == 3:
        print(i)
        exit()