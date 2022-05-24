N = int(input())
B = list(map(int,input().split()))
R = list(map(int,input().split()))

sumB = sum(B)
sumR = sum(R)
print((sumB+sumR)/N)