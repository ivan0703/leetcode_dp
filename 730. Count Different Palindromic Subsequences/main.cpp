#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    int countPalindromicSubsequences(string S) {
        int N = S.length();
        if(N==0) return 0;
        
        int M = 1e9 + 7;

        vector<vector<int>> dp(N, vector<int>(N,0));
        for(int i=0; i<N; i++) {
            dp[i][i] = 1;
        }

        for(int k=1; k<N; k++) {
            for(int i=0; i<N-k; i++) {
                int j = i+k;
                if(S[i]!=S[j]) {
                    dp[i][j] = dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1];
                } else {
                    int left = i+1, right = j-1;
                    while(left<j) {
                        if(S[left]==S[i])
                            break;
                        left++;
                    }
                    while(right>i) {
                        if(S[right]==S[j])
                            break;
                        right--;
                    }

                    if(left>right) {
                        dp[i][j] = dp[i+1][j-1]*2 + 2;
                    } else if(left==right) {
                        dp[i][j] = dp[i+1][j-1]*2 + 1;
                    } else {
                        dp[i][j] = dp[i+1][j-1]*2 - dp[left+1][right-1];
                    }
                }
                dp[i][j] = dp[i][j]<0 ? dp[i][j]+M : dp[i][j]%M;

            }
        }

        return dp[0][N-1];
    }
};

int main()
{
    Solution sol;
    cout<<sol.countPalindromicSubsequences("bccb")<<endl;
    cout<<sol.countPalindromicSubsequences("abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba")<<endl;
    return 0;
}