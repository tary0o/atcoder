S = list(input())

for i in range(2,len(S),2):
    S = S[:-2]
    s1 = S[:len(S)//2]
    s2 = S[len(S)//2:]

    if s1 == s2:
        print(len(S))
        break