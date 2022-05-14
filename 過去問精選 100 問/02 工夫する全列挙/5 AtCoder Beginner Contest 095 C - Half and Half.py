A,B,C,X,Y = map(int,input().split())

minvalue = A*X + Y*B

for i in range( max(X,Y)+1 ):
    value = 0

    if X > i:
        value += A*(X-i)
    if Y > i:
        value += B*(Y-i)

    value += C*(2*i)


    if value < minvalue:
        minvalue = value

print(minvalue)