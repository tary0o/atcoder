N = int(input())
s = set(range(1,2*(N+1)))
print(s.pop(),flush=True)

while True:
    i = int(input())
    s.discard(i)
    print(s.pop(),flush=True)
    if len(s) == 0:
        break