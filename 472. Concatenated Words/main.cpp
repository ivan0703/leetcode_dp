#include <iostream>
#include <vector>
#include <unordered_set>
#include <string>

using namespace std;

class Solution {
public:
    vector<string> findAllConcatenatedWordsInADict(vector<string>& words) {
        unordered_set<string> uset(words.begin(), words.end());
        vector<string> ans;
        for(string word : words) {
            if(word.length()==0)
                continue;
            uset.erase(word);
            vector<bool> dp(word.length()+1, false);
            dp[0] = true;
            for(int i=1; i<=word.length(); i++) {
                for(int j=0; j<i; j++) {
                    if(dp[j] && uset.count(word.substr(j,i-j))) {
                        dp[i] = true;
                        break;
                    }
                }
            }
            uset.insert(word);

            if(dp[word.length()]) {
                ans.push_back(word);
            }
        }
        return ans;
    }
};

int main()
{
    vector<string> words = {
        "cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"
    };

    Solution sol;
    vector<string> ans = sol.findAllConcatenatedWordsInADict(words);
    for(string s : ans) {
        cout<<s<<endl;
    }

    return 0;
}