N = int(input())
count = 0

for i in range( 1,N+1,2 ):
    a = [j for j in range(1,i+1,2) if i%j == 0]
    if len(a) == 8:
        count += 1

print(count)