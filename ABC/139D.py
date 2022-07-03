N = int(input())
if N == 1:
    ans = 0
elif N == 2:
    ans = 1
else:
    ans = (N-1)*N//2
print(ans)