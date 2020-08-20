class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        M, N = len(text1), len(text2)
        dp = [[0 for _ in range(N+1)] for _ in range(M+1)]
        for i in range(1, M+1):
            for j in range(1,N+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        return dp[M][N]

if __name__ == "__main__":
    sol = Solution()
    print(sol.longestCommonSubsequence("abcde","ace"))
    print(sol.longestCommonSubsequence("abc","abc"))
    print(sol.longestCommonSubsequence("abc","def"))