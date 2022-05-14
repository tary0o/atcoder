def primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]

N = int(input())
sosuu = primes(int(N**(1/3)))
preng = len(sosuu)
ans = 0

for i in range(len(sosuu)-1):
    p = sosuu[i]

    if p*(sosuu[i+1])**3 > N:
        break

    ok = i+1
    ng = preng
    while (ng-ok)>1:
        check = (ok+ng)//2
        if p*(sosuu[check])**3 <= N:
            ok = check
        else:
            ng = check
    ng = preng
    ans += ok-i

print(ans)