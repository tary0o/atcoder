abc = list(input())
bca = abc[:]
cab = abc[:]

bca[0] = cab[2] = abc[1]
bca[1] = cab[0] = abc[2]
bca[2] = cab[1] = abc[0]

abc = int(''.join(abc))
bca = int(''.join(bca))
cab = int(''.join(cab))

print(abc+bca+cab)