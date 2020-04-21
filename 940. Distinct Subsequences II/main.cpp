#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    int distinctSubseqII(string S) {
        int M = 1e9 + 7;
        vector<int> dp(S.length(), 0);
        dp[0] = 1;
        for(size_t i=1; i<S.length(); i++) {
            size_t pos = S.find_last_of(S[i], i-1);
            if(pos==string::npos) {
                dp[i] = (dp[i-1]*2 + 1) % M;
            } else {
                dp[i] = dp[i-1]*2 - (pos>0 ? dp[pos-1] : 0);
                dp[i]<0 ? dp[i]+=M : dp[i]%=M;
            }
        }
        return dp[S.length()-1];
    }
};

int main()
{
    Solution sol;
    cout<<sol.distinctSubseqII("abc")<<endl;
    cout<<sol.distinctSubseqII("aba")<<endl;
    cout<<sol.distinctSubseqII("aaa")<<endl;

    return 0;
}