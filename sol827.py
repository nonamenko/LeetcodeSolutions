from typing import List, Dict
from collections import defaultdict
import copy

class Solution:
    def fill(self, grid: List[List[int]], i: int, j: int, number: int) -> int:
        if grid[i][j] != 1:
            return 0
        res = 1
        grid[i][j] = number
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] == 1:
                res += self.fill(grid, ni, nj, number)
        return res

    def largestIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        s = defaultdict(int)
        number = 2
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    s[number] = self.fill(grid, i, j, number)
                    number += 1
        res = max(s.values(), default=0)
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    continue
                r = 1
                seen = set()
                for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < m:
                        island_id = grid[ni][nj]
                        if island_id > 1 and island_id not in seen:
                            r += s[island_id]
                            seen.add(island_id)
                res = max(res, r)
        return res if res > 0 else n * m

    def calculate_island_perimeter(self, grid: List[List[int]], island_id: int) -> int:
        perimeter = 0
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == island_id:
                    for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                        ni, nj = i + di, j + dj
                        if ni < 0 or ni >= n or nj < 0 or nj >= m or grid[ni][nj] != island_id:
                            perimeter += 1
        return perimeter

    def get_island_details(self, grid: List[List[int]]) -> Dict[int, Dict[str, int]]:
        grid_copy = copy.deepcopy(grid)
        s = {}
        number = 2
        n = len(grid_copy)
        m = len(grid_copy[0]) if n > 0 else 0
        for i in range(n):
            for j in range(m):
                if grid_copy[i][j] == 1:
                    s[number] = self.fill(grid_copy, i, j, number)
                    number += 1
        details = {}
        for island_id, area in s.items():
            perimeter = self.calculate_island_perimeter(grid_copy, island_id)
            details[island_id] = {"area": area, "perimeter": perimeter}
        return details
