S = list(range(10))
N =10
x = 3
newS = S[N-x:N]
newS.reverse()
newS = newS + S[0:N-x]
print(newS)