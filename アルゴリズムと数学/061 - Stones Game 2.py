N = int(input())

for i in range(61):
    if (1+2**(i+1)-2)==N:
        print('Second')
        exit()
print('First')