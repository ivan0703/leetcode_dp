#include <iostream>
#include <vector>
#include <climits>

using namespace std;

class SolutionTle {
public:
    int maxProfit(vector<int>& prices) {
        int N = prices.size();
        if(N==0)
            return 0;
        vector<vector<int>> dp(3, vector<int>(N+1,0));
        for(int i=1; i<3; i++) {
            for(int j=1; j<=N; j++) {
                dp[i][j] = dp[i][j-1]; // no transaction on day j
                for(int k=1; k<=j-1; k++) {
                    dp[i][j] = max(dp[i][j], dp[i-1][k-1] + prices[j-1] - prices[k-1]);
                }
            }
        }
        return dp[2][prices.size()];
    }
};

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int N = prices.size();
        if(N==0)
            return 0;
        vector<vector<int>> dp(3, vector<int>(N+1,0));
        for(int i=1; i<3; i++) {
            int maxdiff = INT_MIN;
            for(int j=1; j<=N; j++) {
                dp[i][j] = dp[i][j-1]; // no transaction on day j
                maxdiff = max(maxdiff, dp[i-1][j-1] - prices[j-1]);
                dp[i][j] = max(dp[i][j], maxdiff + prices[j-1]);
            }
        }
        return dp[2][prices.size()];
    }
};

int main()
{   
    vector<int> prices = {3,3,5,0,0,3,1,4};
    SolutionTle soltle;
    cout<<soltle.maxProfit(prices)<<endl;

    Solution sol;
    cout<<sol.maxProfit(prices)<<endl;

    return 0;
}