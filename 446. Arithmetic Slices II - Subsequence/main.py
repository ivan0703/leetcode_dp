from typing import List
from collections import defaultdict

class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        res = 0
        dp = [ defaultdict(int) for _ in range(len(A))]
        for i in range(len(A)):
            for j in range(0, i):
                diff = A[i] - A[j]
                dp[i][diff] += 1
                if diff in dp[j]:
                    res += dp[j][diff]
                    dp[i][diff] += dp[j][diff]
        return res
                


if __name__ == '__main__':
    sol = Solution()
    print(sol.numberOfArithmeticSlices([2,2,3,4]))
    print(sol.numberOfArithmeticSlices([2,4,6,8,10]))