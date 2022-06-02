x1,y1 = map(int,input().split())
x2,y2 = map(int,input().split())
x3,y3 = map(int,input().split())
x4,y4 = map(int,input().split())

s1 = (x2-x1)*(y3-y1)-(x3-x1)*(y2-y1)
t1 = (x2-x1)*(y4-y1)-(x4-x1)*(y2-y1)
s2 = (x4-x3)*(y2-y3)-(x2-x3)*(y4-y3)
t2 = (x4-x3)*(y1-y3)-(x1-x3)*(y4-y3)
ans = 'No'
if s1*t1 < 0 and s2*t2<0:
    ans = 'Yes'
else:
    if s1 == 0 and min(x1,x2)<=x3<=max(x1,x2) and  min(y1,y2)<=y3<=max(y1,y2):
        ans = 'Yes'
    if t1 == 0 and min(x1,x2)<=x4<=max(x1,x2) and  min(y1,y2)<=y4<=max(y1,y2):
        ans = 'Yes'
    if s2 == 0 and min(x3,x4)<=x2<=max(x3,x4) and  min(y3,y4)<=y2<=max(y3,y4):
        ans = 'Yes'
    if t2 == 0 and min(x3,x4)<=x1<=max(x3,x4) and  min(y3,y4)<=y1<=max(y3,y4):
        ans = 'Yes'
print(ans)