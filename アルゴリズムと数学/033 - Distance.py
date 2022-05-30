ax,ay = map(int,input().split())
bx,by = map(int,input().split())
cx,cy = map(int,input().split())

BA = [ax-bx,ay-by]
BC = [cx-bx,cy-by]
CA = [ax-cx,ay-cy]
CB = [bx-cx,by-cy]
BABC = BA[0]*BC[0]+BA[1]*BC[1]
CACB = CA[0]*CB[0]+CA[1]*CB[1]

ab = ( (bx-ax)**2 + (by-ay)**2 )**0.5
bc = ( (bx-cx)**2 + (by-cy)**2 )**0.5
ca = ( (ax-cx)**2 + (ay-cy)**2 )**0.5

if BABC >= 0 and CACB>=0:
    s = (ab+bc+ca)/2
    S = (s*(s-ab)*(s-bc)*(s-ca))**0.5
    print(2*S/bc)
elif BABC < 0:
    print(ab)
else:
    print(ca)