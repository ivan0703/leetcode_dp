from typing import List

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        N = len(stones)
        if N == 0:
            return 0

        total = sum(stones)
        dp = [False] * total + [True]
        for i in range(N):
            for j in range(1,total+1):
                if dp[j] and j-2*stones[i] >= 0:
                    dp[j-2*stones[i]] = True
        res = 0
        for res in range(len(dp)):
            if dp[res]:
                break
        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.lastStoneWeightII([2,7,4,1,8,1]))