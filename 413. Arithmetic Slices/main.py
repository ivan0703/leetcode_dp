from typing import List

class Solution:
    def numberOfArithmeticSlices_slow(self, A: List[int]) -> int:
        dp = [[False] * len(A) for _ in range(len(A))]
        cnt = 0
        for i in range(len(A)-2):
            if A[i+2]-A[i+1]==A[i+1]-A[i]:
                dp[i][i+2] = True
                cnt = cnt + 1
        print(dp)
        for k in range(3, len(A)):
            for i in range(len(A)-k):
                j = i + k
                dp[i][j] = dp[i][j-1] and dp[i+1][j]
                print('dp[{0}][{1}]={2}'.format(i,j,dp[i][j]))
                if dp[i][j]:
                    cnt = cnt+1
        return cnt

    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        res = 0
        dp = 0
        for i in range(2,len(A)):
            if A[i]-A[i-1]==A[i-1]-A[i-2]:
                dp += 1
                res += dp
            else:
                dp = 0
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.numberOfArithmeticSlices([1,2,3,4]))