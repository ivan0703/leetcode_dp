from typing import List

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if len(stones)<2 or stones[0]!=0 or stones[1]!=1:
            return False

        umap = {}
        for i,s in enumerate(stones):
            umap[s] = i
        dp = [set() for _ in range(len(stones))]
        dp[1].add(1)
        for i in range(1, len(stones)-1):
            for s in dp[i]:
                if s-1 > 0 and (stones[i]+s-1) in umap:
                    dp[umap[stones[i]+s-1]].add(s-1)
                if stones[i]+s in umap:
                    dp[umap[stones[i]+s]].add(s)
                if stones[i]+s+1 in umap:
                    dp[umap[stones[i]+s+1]].add(s+1)

        return len(dp[len(stones)-1]) > 0

if __name__ == "__main__":
    sol = Solution()
    print(sol.canCross([0,1,3,5,6,8,12,17]))
    print(sol.canCross([0,1,2,3,4,8,9,11]))
    print(sol.canCross([0,2]))