import numpy as np
N = int(input())

for i in range(1,int(np.sqrt(N))+1):
    if N%i == 0:
        print(i)
        if i != N/i:
            print(int(N/i))