from typing import List

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        N = len(envelopes)
        envelopes.sort()
        dp = [1] * N
        for i in range(1,N):
            for j in range(i-1,-1,-1):
                if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxEnvelopes([]))
    print(sol.maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]))
    print(sol.maxEnvelopes([[1,5],[2,3],[5,4],[6,6],[6,7]]))