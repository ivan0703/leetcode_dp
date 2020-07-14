from typing import List, Dict
import bisect

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = {}
        return self.subcost(0, dp, days, costs)

    def subcost(self, start: int, dp: Dict[int, int], days: List[int], costs: List[int]) -> int:
        if start in dp:
            return dp[start]
        elif start >= len(days):
            return 0
        
        ans = float('Inf')
        d = [1,7,30]
        for i in range(len(costs)):
            next = bisect.bisect_right(days, days[start]+d[i]-1)
            ans = min(ans, costs[i] + self.subcost(next, dp, days, costs))
        dp[start] = ans
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.mincostTickets([1,4,6,7,8,20], [2,7,15]))
    print(sol.mincostTickets([1,2,3,4,5,6,7,8,9,10,30,31], [2,7,15]))
