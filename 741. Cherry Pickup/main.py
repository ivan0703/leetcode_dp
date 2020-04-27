from typing import List
from collections import defaultdict

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        if len(grid)==0 or len(grid[0])==0:
            return 0
        M, N = len(grid), len(grid[0])
        dp = defaultdict(lambda: -1)

        # two player both start from (0,0)
        q = {(0,0)}
        dp[(0,0,0,0)] = grid[0][0]
        while q:
            nset = set()
            lst = list(q)
            for i in range(len(lst)):
                x1,y1 = lst[i][0], lst[i][1]
                if grid[x1][y1] == -1:
                    continue
                nset.add((x1+1, y1)) if x1 + 1 < M else None
                nset.add((x1, y1+1)) if y1 + 1 < N else None

                for j in range(0,i+1):
                    x2,y2 = lst[j][0], lst[j][1]
                    if grid[x2][y2] == -1:
                        continue

                    if x1-1>=0 and x2-1>=0:
                        dp[(x1,y1,x2,y2)] = max(dp[(x1,y1,x2,y2)], dp[(x1-1,y1,x2-1,y2)])
                    if x1-1>=0 and y2-1>=0:
                        dp[(x1,y1,x2,y2)] = max(dp[(x1,y1,x2,y2)], dp[(x1-1,y1,x2,y2-1)])
                    if y1-1>=0 and x2-1>=0:
                        dp[(x1,y1,x2,y2)] = max(dp[(x1,y1,x2,y2)], dp[(x1,y1-1,x2-1,y2)])
                    if y1-1>=0 and y2-1>=0:
                        dp[(x1,y1,x2,y2)] = max(dp[(x1,y1,x2,y2)], dp[(x1,y1-1,x2,y2-1)])
                    
                    if (x1,y1,x2,y2) != (0,0,0,0) and dp[(x1,y1,x2,y2)] >= 0:
                        if (x1,y1) != (x2,y2):
                            dp[(x1,y1,x2,y2)] += grid[x1][y1] + grid[x2][y2]
                        else:
                            dp[(x1,y1,x2,y2)] += grid[x1][y1]
                        dp[(x2,y2,x1,y1)] = dp[(x1,y1,x2,y2)]
            q = nset

        return max(dp[M-1,N-1,M-1,N-1], 0)

if __name__ == '__main__':
    grid1 = [
        [0, 1, -1],
        [1, 0, -1],
        [1, 1,  1]
    ]

    grid2 = [
        [1,1,-1],
        [1,-1,1],
        [-1,1,1]
    ]

    grid3 = [
        [1,1,0,0],
        [0,1,0,1],
        [1,1,0,0],
        [0,1,1,1]
    ]

    grid4 = [
        [1,1,1,1,0,0,0],
        [0,0,0,1,0,0,0],
        [0,0,0,1,0,0,1],
        [1,0,0,1,0,0,0],
        [0,0,0,1,0,0,0],
        [0,0,0,1,0,0,0],
        [0,0,0,1,1,1,1]
    ]

    sol = Solution()
    print(sol.cherryPickup(grid1))
    print(sol.cherryPickup(grid2))
    print(sol.cherryPickup(grid3))
    print(sol.cherryPickup(grid4))