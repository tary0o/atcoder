import heapq
from sys import exit
class HeapDict:
    def __init__(self):
        self.h=[]
        self.d=dict()

    def insert(self,x):
        heapq.heappush(self.h,x)
        if x not in self.d:
            self.d[x]=1
        else:
            self.d[x]+=1

    def erase(self,x):
        if x not in self.d or self.d[x]==0:
            print(x,"is not in HeapDict")
            exit()
        else:
            self.d[x]-=1

        while len(self.h)!=0:
            if self.d[self.h[0]]==0:
                heapq.heappop(self.h)
            else:
                break

    def is_exist(self,x):
        if x in self.d and self.d[x]!=0:
            return True
        else:
            return False

    def get_min(self):
        return self.h[0]

Q = int(input())
S = {}
s = HeapDict()
minus_s = HeapDict()
ans = []

for i in range(Q):
    ixc = list(map(int,input().split()))
    if ixc[0]==1:
        x = ixc[1]
        if x in S:
            S[x] += 1
        else:
            S[x] = 1
            s.insert(x)
            minus_s.insert(-x)
        

    if ixc[0]==2:
        x,c = ixc[1],ixc[2]
        if x in S:
            if c>=S[x]:
                del S[x]
                s.erase(x)
                minus_s.erase(-x)
            else:
                S[x] -= c
    
    if ixc[0]==3:
        ans.append(-minus_s.get_min() - s.get_min())
for a in ans:
    print(a)