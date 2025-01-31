class Solution:
    def fill(self, grid: [], i: int, j: int, number: int) -> int:
        if grid[i][j] == 0:
            return 0
        res = 1
        grid[i][j] = number
        if i > 0 and grid[i-1][j] == 1:
            res += self.fill(grid, i-1, j, number)
        if j > 0 and grid[i][j-1] == 1:
            res += self.fill(grid, i, j-1, number)
        if i + 1 < len(grid) and grid[i+1][j] == 1:
            res += self.fill(grid, i+1, j, number)
        if j + 1 < len(grid[0]) and grid[i][j+1] == 1:
            res += self.fill(grid, i, j+1, number)

        return res

    def largestIsland(self, grid: List[List[int]]) -> int:
        s = defaultdict(int)
        number = 2
        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    s[number] = self.fill(grid, i, j, number)
                    number += 1
        
        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    continue
                r = 1
                r_s = set()
                if i > 0 and grid[i-1][j] != 0:
                    r += s[grid[i-1][j]]
                    r_s.add(grid[i-1][j])
                if j > 0 and grid[i][j-1] != 0 and grid[i][j-1] not in r_s:
                    r += s[grid[i][j-1]]
                    r_s.add(grid[i][j-1])
                if i + 1 < n and grid[i+1][j] != 0 and grid[i+1][j] not in r_s:
                    r += s[grid[i+1][j]]
                    r_s.add(grid[i+1][j])
                if j +1 < m and grid[i][j+1] != 0 and grid[i][j+1] not in r_s:
                    r += s[grid[i][j+1]]

                res = max(res, r)

        return res if res > 0 else n*m