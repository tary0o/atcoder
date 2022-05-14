x1,y1,x2,y2 = map(int,input().split())

if (x1 == x2) and (abs(y1-y2)==2 or abs(y1-y2)==4):
    print('Yes')
elif (abs(x1-x2)==1) and (abs(y1-y2)==1 or abs(y1-y2)==3):
    print('Yes')
elif (abs(x1-x2)==2) and (y1==y2 or abs(y1-y2)==4):
    print('Yes')
elif (abs(x1-x2)==3) and (abs(y1-y2)==1 or abs(y1-y2)==3):
    print('Yes')
elif (abs(x1-x2)==4) and (y1==y2 or abs(y1-y2)==2):
    print('Yes')
else:
    print('No')