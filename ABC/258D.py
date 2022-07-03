N,X = map(int,input().split())
sumA = [0]
sumB = [0]
B = [0]
for i in range(1,N+1):
    Ai,Bi = map(int,input().split())
    sumA.append(sumA[i-1] + Ai)
    sumB.append(sumB[i-1] + Bi)
    B.append(Bi)

ans = int(1e30)
for i in range(1,N+1): 
    if i>X:
        break
    time = 0
    time += sumA[i]
    time += sumB[i-1]
    time += B[i]*(X+1-i)
    ans = min(time,ans)
print(ans)