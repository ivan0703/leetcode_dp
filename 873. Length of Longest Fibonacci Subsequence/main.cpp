#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    int lenLongestFibSubseq(vector<int>& A) {
        if(A.size()<3)
            return 0;

        unordered_map<int,int> umap;
        int res = 2;
        int N = A.size();
        vector<vector<int>> dp(N, vector<int>(N, 2));
        for(int i=0; i<N; i++) {
            umap[A[i]] = i;
            for(int j=i-1; j>=0; j--) {
                int diff = A[i] - A[j];
                if(diff<A[j] && umap.count(diff)>0) {
                    dp[i][j] = dp[j][umap[diff]] + 1;
                    res = max(res, dp[i][j]);
                }
            }
        }
        return res>=3 ? res : 0;
    }
};

int main()
{
    vector<int> nums1 = {1,2,3,4,5,6,7,8}; // 5
    vector<int> nums2 = {1,3,7,11,12,14,18}; // 3
    vector<int> nums3 = {2,4,5,6,7,8,11,13,14,15,21,22,34}; // 5
    vector<int> nums4 = {2,4,7,8,9,10,14,15,18,23,32,50}; // 5
    
    Solution sol;
    cout<<sol.lenLongestFibSubseq(nums1)<<endl;
    cout<<sol.lenLongestFibSubseq(nums2)<<endl;
    cout<<sol.lenLongestFibSubseq(nums3)<<endl;
    cout<<sol.lenLongestFibSubseq(nums4)<<endl;

    return 0;
}