N = int(input())
expected_value = 0

for _ in range(N):
    p,q = map(int,input().split())
    expected_value  += q/p
print(expected_value)