N = int(input())
T = input()

muki = 'Higasi'
x,y = 0,0
for i in range(N):
    if T[i] == 'S':
        if muki =='Higasi':
            x += 1
        elif muki == 'Nisi':
            x -= 1
        elif muki == 'Kita':
            y += 1
        elif muki == 'Minami':
            y -= 1
    else:
        if muki =='Higasi':
            muki = 'Minami'
        elif muki == 'Nisi':
            muki = 'Kita'
        elif muki == 'Kita':
            muki = 'Higasi'
        elif muki == 'Minami':
            muki = 'Nisi'

print(x,y)