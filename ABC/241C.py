N = int(input())
s = [ input() for _ in range(N)]
ans = 'No'

for x in range(N):
    for y in range(N-5):
        cnt = 0
        for i in range(6):
            if s[x][y+i] == '#':
                cnt += 1
        if cnt >= 4:
            print('Yes')
            exit()

for y in range(N):
    for x in range(N-5):           
        cnt = 0
        for i in range(6):
            if s[x+i][y] == '#':
                cnt += 1
        if cnt >= 4:
            print('Yes')
            exit()

for x in range(N-5):
    for y in range(N-5):
        cnt = 0
        for i in range(6):
            if s[x+i][y+i] == '#':
                cnt += 1
        if cnt >= 4:
            print('Yes')
            exit()

for x in range(1,N-4):
    for y in range(N-5):
        cnt = 0
        for i in range(6):
            if s[-x-i][y+i] == '#':
                cnt += 1
        if cnt >= 4:
            print('Yes')
            exit()

print('No')