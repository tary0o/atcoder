N = int(input())
s,t = list(),list()
test = set()
test2 = set()
ans = 'Yes'

for _ in range(N):
    si,ti = input().split()
    s.append(si)
    t.append(ti)

    if si in test:
        test2.add(si)
    else:
        test.add(si)
    if si != ti:
        if ti in test:
            test2.add(ti)
        else:
            test.add(ti)
    
for i in range(N):
    if s[i] in test2 and t[i] in test2:
        ans = 'No'

print(ans)