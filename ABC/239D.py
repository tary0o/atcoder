def sosuu(n):
    if n==2 or n == 3 or n== 5:
        return True

    if n%2 == 0 or n==1:
        return False
    
    for i in range(3,int(n/2),2):
        if n%i == 0:
            return False
    
    return True

A,B,C,D = map(int,input().split())
for i in range(A,B+1):
    count = 0
    for j in range(C,D+1):
        if not sosuu(i+j):
            count += 1
    if count == (D-C+1):
        print('Takahashi')
        exit()
print('Aoki')