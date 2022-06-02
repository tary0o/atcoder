import math
A,B,H,M = map(int,input().split())

pi = math.pi
Hsita = 2*pi*(60*H+M)/720
Msita = 2*pi*M/60

Hx = A*math.cos(Hsita)
Hy = A*math.sin(Hsita)
Mx = B*math.cos(Msita)
My = B*math.sin(Msita)

print(((Hx-Mx)**2+(Hy-My)**2)**0.5)