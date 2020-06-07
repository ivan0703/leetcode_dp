from typing import List

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1)==0 or len(s1)!=len(s2):
            return False

        N = len(s1)
        dp = [[[False for _ in range(N)] for _ in range(N)] for _ in range(N)]
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    if i + k >= N or j + k >= N:
                        continue
                    if k == 0:
                        dp[i][j][k] = (s1[i]==s2[j])
                    else:
                        if ''.join(sorted(s1[i:i+k+1])) != ''.join(sorted(s2[j:j+k+1])):
                            dp[i][j][k] = False
                            continue
                        
                        for m in range(k):
                            dp[i][j][k] |= dp[i][j][m] and dp[i+m+1][j+m+1][k-m-1]
                            dp[i][j][k] |= dp[i][j+k-m][m] and dp[i+m+1][j][k-m-1]
        return dp[0][0][N-1]

if __name__ == "__main__":
    sol = Solution()
    print(sol.isScramble("great", "rgeat"))
    print(sol.isScramble("great", "taerg"))
    print(sol.isScramble("abcde", "caebd"))
    print(sol.isScramble("abc", "acb"))