x1,y1,r1 = map(float,input().split())
x2,y2,r2 = map(float,input().split())

dist = ((x1-x2)**2+(y1-y2)**2)**0.5

if dist < abs(r1-r2):
    print(1)
elif dist == abs(r1-r2):
    print(2)
elif abs(r1-r2) < dist < r1+r2:
    print(3)
elif dist == r1+r2:
    print(4)
else:
    print(5)