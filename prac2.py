"""
grid = [[1,3,1],[1,5,1],[4,2,1]]
grid1 = [[1,2,3],[4,5,6]]
x = 0
for i in range(len(grid)):
    for j in range(len(grid[1])):
        if i == 0:
            x = x + grid[i][j]
        else:
            x = x + grid[i][-1]
            break
print(x)
"""

class Solution:
    def minPathSum(self, grid):
        x = 0
        for i in range(len(grid)):
            for j in range(len(grid[1])):
                if i == 0 and len(grid[i]) != 2:
                    x = x + grid[i][j]
                else:
                    x = x + grid[i][-1]
                    break
        return x

x = Solution()
print(x.minPathSum([[1,2,5],[3,2,1]]))

m = [[1,2],[1,1]]
print(len(m[1]))




