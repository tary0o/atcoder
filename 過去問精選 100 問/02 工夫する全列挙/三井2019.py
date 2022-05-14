N = int(input())
S = input()
ans = 0

for num in range(1000):
    s = str(num)

    if num < 10:
        i,j,k = '0','0',s[0]
    elif num < 100:
        i,j,k = '0',s[0],s[1]
    else:
        i,j,k = s[0],s[1],s[2]

    left = S.find(i)
    center = S.find(j,left+1)
    right = S.find(k,center+1)

    if left >= 0 and center > 0 and right > 0:
        ans += 1

  
print(ans)