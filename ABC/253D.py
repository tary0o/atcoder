import math
N,A,B = map(int,input().split())

gcd = math.gcd(A,B)
lcm = A*B//gcd
numA,numB,numlcm = N//A,N//B,N//lcm

sum = N*(N+1)//2
sumA = numA*(numA*A+A)//2
sumB = numB*(numB*B+B)//2
sumlcm = numlcm*(numlcm*lcm+lcm)//2

print(int(sum-sumA-sumB+sumlcm))