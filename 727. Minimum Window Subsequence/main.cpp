#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    string minWindow(string S, string T) {
        int M = S.length();
        int N = T.length();

        if(M==0 || N==0)
            return "";
        
        vector<vector<pair<int,int>>> dp(N+1, vector<pair<int,int>>(M+1, {0,0}));
        for(int i=1; i<=N; i++) {
            for(int j=1; j<=M; j++) {
                if(T[i-1]==S[j-1] && (i==1 || dp[i-1][j-1].first!=0)) {
                    dp[i][j].first = j;
                    dp[i][j].second = (i==1 ? 1 : j-dp[i-1][j-1].first + dp[i-1][j-1].second);
                } else {
                    dp[i][j] = dp[i][j-1];
                }
            }
        }

        int idx = -1;
        int minWin = INT_MAX;
        for(int j=1; j<=M; j++) {
            if(dp[N][j].second>0 && dp[N][j].second<minWin) {
                minWin = dp[N][j].second;
                idx = j;
            }
        }

        return idx==-1 ? "" : S.substr(idx-minWin, minWin);
    }
};

int main()
{
    Solution sol;
    cout<<sol.minWindow("abcdebdde","bde")<<endl;
    cout<<sol.minWindow("abcdebdde","b")<<endl;
    cout<<sol.minWindow("zmccmj","mm")<<endl;
    cout<<sol.minWindow("cnhczmccqouqadqtmjjzl","mm")<<endl;
    cout<<sol.minWindow("fgrqsqsnodwmxzkzxwqegkndaa","fnok")<<endl;
    return 0;
}