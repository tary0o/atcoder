P =float(input())

high = P
low = 0

f = lambda x : x + P*2**(-x/1.5)

while high-low>10**(-9):
    c1 = (low*2+high)/3
    c2 = (low+high*2)/3

    if f(c1) >= f(c2):
        low = c1
    else:
        high = c2
print(f(low))