N = int(input())
tutu = []
count = 1
index = 0
a = list(map(int,input().split()))

for i in range(0,N):
    tutu.append(a[i])

    if i > 0:
        if tutu[index] == tutu[index-1]:
            count += 1
        else:
            count = 1
    
    if count == a[i]:
        for j in range(count):
            tutu.pop()
        index -= count
        if len(tutu)==0:
            count = 0
        else:
            count = 1
            for j in range(index):
                if tutu[index-j] == tutu[index-j-1]:
                    count += 1
                else:
                    break

    index += 1

    print(len(tutu))