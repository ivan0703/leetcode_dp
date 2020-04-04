#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        int M = text1.length();
        int N = text2.length();
        
        vector<vector<int>> dp(M+1, vector<int>(N+1,0));
        for(int i=1; i<=M; i++) {
            for(int j=1; j<=N; j++) {
                if(text1[i-1]==text2[j-1]) {
                    dp[i][j] = dp[i-1][j-1] + 1;
                } else {
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1]);
                }
            }
        }
        
        return dp[M][N];
    }
};

int main()
{
    string text1 = "abcde";
    string text2 = "ace";

    Solution sol;
    cout<<sol.longestCommonSubsequence(text1, text2)<<endl;

    return 0;
}