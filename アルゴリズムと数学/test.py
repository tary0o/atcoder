import math
# 入力
N, K = map(int, input().split())
V = list(map(int, input().split()))

# ビット全探索
Answer = 0
for i in range(1, 1 << K):
	cnt = -1
	lcm = 1
	for j in range(K):
		if (i & (1 << j)) != 0:
			cnt *= -1
			lcm = (lcm*V[j])//math.gcd(lcm,V[j])
			
	# num は N 以下の中で選ばれたすべての倍数であるものの個数
	num = N // lcm
	Answer += cnt*(num)
# 出力
print(Answer)