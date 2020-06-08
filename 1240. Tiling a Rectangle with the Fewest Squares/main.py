from typing import List

class Solution:
    def __init__(self):
        self.n = 0
        self.m = 0
        self.ans = 0

    def dfs(self, cur: int, fill: List):
        if cur > self.ans:
            return

        (h, start) = min((v,i) for (i,v) in enumerate(fill))
        if h == self.n:
            self.ans = min(self.ans, cur)
            return
        
        end = start
        while end<self.m and fill[end]==fill[start] and h+end-start<self.n:
            end += 1
        
        while end > start:
            e = end - start
            for i in range(start,end):
                fill[i] += e
            self.dfs(cur+1, fill)
            for i in range(start,end):
                fill[i] -= e
            end -= 1

    def tilingRectangle(self, n: int, m: int) -> int:
        if n > m:
            return self.tilingRectangle(m, n)
        if n == m:
            return 1
        
        self.n = n
        self.m = m
        self.ans = n * m
        
        fill = [0] * m
        self.dfs(0, fill)
        return self.ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.tilingRectangle(2,3))
    print(sol.tilingRectangle(5,8))
    print(sol.tilingRectangle(11,13))
