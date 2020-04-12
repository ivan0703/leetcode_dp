#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> largestDivisibleSubset(vector<int>& nums) {
        int N = nums.size();
        if(N==0) return {};
        sort(nums.begin(),nums.end());
        vector<pair<int,int>> dp(N,{0,0});
        dp[0] = {0,1};
        for(int i=1; i<N; i++) {
            dp[i] = {i,1};
            for(int j=i-1; j>=0; j--) {
                if(nums[i]%nums[j]==0 && dp[i].second<dp[j].second+1) {
                    dp[i].first = j;
                    dp[i].second = dp[j].second+1;
                }
            }
        }

        // find max group
        int max_num = 0, idx = -1;
        for(int i=N-1; i>=0; i--) {
            if(dp[i].second>max_num) {
                max_num = dp[i].second;
                idx = i;
            }
        }

        // construct result
        vector<int> res;
        while(dp[idx].first!=idx) {
            res.push_back(nums[idx]);
            idx = dp[idx].first;
        }
        res.push_back(nums[idx]);

        return res;
    }
};

int main()
{
    //vector<int> nums = {1,2,3};
    vector<int> nums = {4,8,10,240};
    Solution sol;
    vector<int> res = sol.largestDivisibleSubset(nums);
    for(int i : res) {
        cout<<i<<", ";
    }
    cout<<endl;

    return 0;
}