from typing import List

class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        if len(A) < 3:
            return 0
        res = 2
        dp = [[2]*len(A) for i in range(len(A))]

        idx = {}
        for i in range(len(A)):
            idx[A[i]] = i
            for j in range(i):
                diff = A[i] - A[j]
                if (diff<A[j]) and (diff in idx):
                    dp[i][j] = dp[j][idx[diff]] + 1
                    res = max(res, dp[i][j])

        return res if res > 2 else 0

if __name__ == '__main__':
    nums = [1,2,3,4,5,6,7,8]
    sol = Solution()
    print(sol.lenLongestFibSubseq(nums))