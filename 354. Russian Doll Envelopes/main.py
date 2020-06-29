from typing import List
from functools import cmp_to_key
import bisect

class Solution:
    def maxEnvelopes_tle(self, envelopes: List[List[int]]) -> int:
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

    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=cmp_to_key(lambda x,y: -1 if x[0]<y[0] or (x[0]==y[0] and x[1]>y[1]) else 1))
        dp = []
        for i in range(len(envelopes)):
            p = bisect.bisect_left(dp, envelopes[i][1])
            if p == len(dp):
                dp.append(envelopes[i][1])
            else:
                dp[p] = envelopes[i][1]
        return len(dp)

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxEnvelopes([]))
    print(sol.maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]))
    print(sol.maxEnvelopes([[1,5],[2,3],[5,4],[6,6],[6,7]]))

    print("TLE version:")
    print(sol.maxEnvelopes_tle([]))
    print(sol.maxEnvelopes_tle([[5,4],[6,4],[6,7],[2,3]]))
    print(sol.maxEnvelopes_tle([[1,5],[2,3],[5,4],[6,6],[6,7]]))