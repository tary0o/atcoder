def multiply(A,B):
	n = len(A)
	print(n)
	C = [[0]*n for _ in range(n)]
	for i in range(n):
		for j in range(n):
			for k in range(n):
				C[i][j] += A[i][k]*B[k][j]
	return C

A = [[1,1,1],[2,0,1],[2,1,1]]
B = [[2,2,1],[3,0,1],[1,1,1]]
C = multiply(A,B)

print(C)