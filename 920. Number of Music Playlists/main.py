class Solution:
    def numMusicPlaylists(self, N: int, L: int, K: int) -> int:
        if L < N:
            return 0

        M = 10**9 + 7
        # dp[i][j]: list of length i and contains j different songs
        dp = [[0 for _ in range(N+1)] for _ in range(L+1)]
        dp[0][0] = 1
        for i in range(1,L+1):
            for j in range(1,N+1):
                dp[i][j] = (dp[i-1][j-1] * (N-j+1)) % M
                if j > K:
                    dp[i][j] += dp[i-1][j] * (j-K)
                    dp[i][j] %= M
        return dp[L][N]

if __name__ == "__main__":
    sol = Solution()
    print(sol.numMusicPlaylists(3,3,0))
    print(sol.numMusicPlaylists(2,3,0))
    print(sol.numMusicPlaylists(2,3,1))