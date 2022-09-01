rows = len(grid)
cols = len(grid[0])
visited = set()
directions = [[0,1], [0,-1], [-1,0], [1,0]]
def dfs(r, c):
    # if row and col 越界： return
    # if row and col visited: return
    if not (0<=r<rows) or not (0<=c<cols) or (row, col) in visited:
        return
    # 标记为访问过
    visited.add(r, c)
    for dr, dc in directions:
        row = r+dr
        col = c+dc
        dfs(row, col)

# 多点搜索
for i in range(r):
   for j in range(N):
      dfs(i, j)