class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string ans="";
        if(strs.size() == 0) return ans;
        int sz = 10000;
        for(string x : strs){
            sz = (x.size() < sz) ? x.size() : sz; 
        }
        for(int i = 0 ; i < sz ; i++){
            char c;
            c = strs[0][i];
            for(string x : strs){
                if(x[i] != c){
                    return ans;
                }
            }
            if(strs[0].size() > 0){
                ans += c;
            }
        }
        return ans;
    }
};