N,Q = map(int,input().split())
x = [int(input()) for _ in range(Q)]
a = list(range(N+1))
a_index = list(range(N+1))

for q in x:
    index = a_index[q]
    if index < N:
        tmp = a[index]
        a[index] = a[index+1]
        a[index+1] = tmp

        a_index[a[index]] = index
        a_index[q] = index+1
    
    else:
        tmp = a[index]
        a[index] = a[index-1]
        a[index-1] = tmp
    
        a_index[a[index]] = index
        a_index[q] = index-1

print(*a[1:])