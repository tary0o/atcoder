from re import I


A,B = map(int,input().split())

ans = 1
for i in range(2,B+1):
    a = A//i
    if A%i != 0:
        a += 1
    b = B//i
    if A <= a*i < b*i <=B:
        ans = i
print(ans)