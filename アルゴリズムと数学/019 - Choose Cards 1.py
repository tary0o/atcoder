N = int(input())
A = list(map(int,input().split()))
color = [0]*4

for a in A:
    color[a] += 1

cnt = color[1]*(color[1]-1)/2 + color[2]*(color[2]-1)/2 + color[3]*(color[3]-1)/2
print(int(cnt))