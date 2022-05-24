A,B = map(int,input().split())

big = max(A,B)
small = min(A,B)

while small != 0:
    tmp = big%small
    big = max(tmp,small)
    small = min(tmp,small)
print(big)