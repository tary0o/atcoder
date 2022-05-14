S = input()
fronta = 0
backa = 0

for i in range( len(S) ):
    if S[i] == 'a':
        fronta += 1
    else:
        break

for i in range( len(S)):
    if S[len(S)-i-1] == 'a':
        backa += 1
    else:
        break
dif = backa - fronta
if dif < 0:
	exit(print("No"))
else:
    S = S[ 0 : len(S)-dif]
    for i in range( len(S) ):
        if S[i] != S[len(S)-i-1]:
            exit(print("No"))

print('Yes')