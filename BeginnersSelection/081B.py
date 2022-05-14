N = int(input())
A = list( map(int,input().split()) )

count = 0
loop = True

while loop:
    for i in range(N):
        if A[i] % 2 == 1:
            loop = False
        A[i] /= 2
    count += 1
count -= 1

print(count)