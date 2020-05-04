from typing import List

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if len(stones)<2 or stones[0]!=0 or stones[1]!=1:
            return False

        dp = {}
        for s in stones:
            dp[s] = set()
        dp[1].add(1)
        for i in range(1, len(stones)-1):
            for s in dp[stones[i]]:
                if s-1 > 0 and (stones[i]+s-1) in dp:
                    dp[stones[i]+s-1].add(s-1)
                if stones[i]+s in dp:
                    dp[stones[i]+s].add(s)
                if stones[i]+s+1 in dp:
                    dp[stones[i]+s+1].add(s+1)

        return len(dp[stones[-1]]) > 0

if __name__ == "__main__":
    sol = Solution()
    print(sol.canCross([0,1,3,5,6,8,12,17]))
    print(sol.canCross([0,1,2,3,4,8,9,11]))
    print(sol.canCross([0,2]))