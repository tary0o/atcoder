import itertools

m = int(input())
n = int(input())
ice = []
stack = []
ans = 0
dhdw = [[1,0],[-1,0],[0,1],[0,-1]]

for i in range(n):
    ice.append( list(map(int,input().split())) )

for H,W in itertools.product(range(n),range(m)):
    if ice[H][W] == 1:
        stack.append([[H,W],set()])

        while stack:
            [sh,sw],history = stack.pop()
            ans = max(ans,len(history))
            
            for dh,dw in dhdw:
                h,w = sh+dh,sw+dw
                if  0<=h<n and 0<=w<m and not((h,w)in history) and ice[h][w] == 1:
                    stack.append([[h,w],history | {(h,w)}])
print(ans)