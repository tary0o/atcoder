K = int(input())
H = str(21+K//60)
M = str(K%60)
if len(M)==1:
    M = '0'+M
ans = H+':'+M
print(ans)