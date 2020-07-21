class Solution:
    def minCut(self, s: str) -> int:
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True

        for k in range(1,len(s)):
            for i in range(0,len(s)-k):
                j = i + k
                if s[i] == s[j]:
                    dp[i][j] = True if j==i+1 else dp[i+1][j-1]

        return self.cutNum(dp)

    def cutNum(self, pd):
        dp = [-1] + [float('Inf')] * len(pd)
        for j in range(1,len(dp)):
            for i in range(1,j+1):
                if pd[i-1][j-1]:
                    dp[j] = min(dp[j], dp[i-1]+1)
        return dp[-1]

if __name__ == "__main__":
    sol = Solution()
    print(sol.minCut("aaba"))
    print(sol.minCut("aab"))
    print(sol.minCut("abbab"))
    print(sol.minCut("aaba"))
    print(sol.minCut("aaabaa"))
    print(sol.minCut("a"*1000))
    print(sol.minCut("a"*200 + "bb" + "a"*210)) # slow
