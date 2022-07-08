N,K = map(int,input().split())
A = list(map(int,input().split()))

sumA= sum(A)

if sumA<=K and (K-sumA)%2==0:
    print('Yes')
else:
    print('No')