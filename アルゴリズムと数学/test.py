A = list(map(int,input().split()))

def hoge(C):
    C[0] = 3
    return C

B= hoge(A)
print(A)
print(B)