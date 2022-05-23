import numpy as np

N = int(input())

for i in range(2,int(np.sqrt(N))):
    if N%i == 0:
        print('No')
        exit()
print('Yes')