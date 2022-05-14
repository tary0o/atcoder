N = int(input())
x,y = [],[]
for _ in range(N):
    xi,yi = map(int,input().split())
    x.append(xi)
    y.append(yi)
S = input()

leftmax,rightmin = dict(),dict()
ans = 'No'
for i in range(N):
    if S[i] == 'L':
        if y[i] in rightmin and rightmin[y[i]] < x[i]:
            ans = 'Yes'
            break
        else:
            if y[i] in leftmax:
                leftmax[y[i]] = max( x[i],leftmax[y[i]] )
            else:
                leftmax[y[i]] = x[i]
    else:
        if y[i] in leftmax and leftmax[y[i]] > x[i]:
            ans = 'Yes'
            break
        else:
            if y[i] in rightmin:
                rightmin[y[i]] = min( x[i],rightmin[y[i]] )
            else:
                rightmin[y[i]] = x[i]
    
print(ans)