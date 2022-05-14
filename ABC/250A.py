H,W = map(int,input().split())
R,C = map(int,input().split())

ans = 0
if 1 <= R+1 <= H and 1<= C <= W:
    ans += 1
if 1 <= R-1 <= H and 1<= C <= W:
    ans += 1
if 1 <= R <= H and 1<= C+1 <= W:
    ans += 1
if 1 <= R <= H and 1<= C-1 <= W:
    ans += 1
print(ans)