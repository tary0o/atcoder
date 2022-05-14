import itertools

while True:
    w,h = map(int,input().split())
    if w == h == 0:
        exit()
    c = [ list(map(int,input().split())) for _ in range(h) ]
    ans = 0
    seen = [ [0]*w for _ in range(h) ]
    stack = []
    dhdw = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]

    for H,W in itertools.product(range(h),range(w)):
        if seen[H][W] == 1 or c[H][W] == 0:
            continue

        ans += 1
        seen[H][W] = 1
        stack.append([H,W])

        while stack:
            sh,sw = stack.pop()
            for dh,dw in dhdw:
                nh,nw = sh+dh,sw+dw

                if not(0<=nh<=h-1) or not(0<=nw<=w-1):
                    continue
                if seen[nh][nw] == 1 or c[nh][nw] == 0:
                    continue
                seen[nh][nw] = 1
                stack.append([nh,nw])

    print(ans)