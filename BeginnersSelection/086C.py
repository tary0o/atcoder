N = int(input())

pt,px,py = 0,0,0
for i in range(N):
    t,x,y = map(int,input().split())

    if (t%2 != (x+y)%2) or (t-pt < abs(x-px) + abs(y-py)):
        print('No')
        exit()

    pt,px,py = t,x,y
print('Yes')