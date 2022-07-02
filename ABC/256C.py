tmp = list(map(int,input().split()))
h = [0] + tmp[0:3]
w = [0] + tmp[3:6]
ans = 0

for x1y1 in range(1,h[1]-1):
    for x2y1 in range(1,h[1]-x1y1):
        for x1y2 in range(1,h[2]-1):
            for x2y2 in range(1,h[2]-x1y2):
                x3y1 = h[1]-(x1y1+x2y1)
                x3y2 = h[2]-(x1y2+x2y2)
                x1y3 = w[1]-(x1y1+x1y2)
                x2y3 = w[2]-(x2y1+x2y2)
                x3y3 = h[3]-(x1y3+x2y3)
                if x1y3<=0 or x2y3<=0 or x3y3<=0:
                    continue
                if (x1y3+x2y3+x3y3)==h[3]  and (x3y1+x3y2+x3y3)==w[3]:
                    ans += 1
print(ans)