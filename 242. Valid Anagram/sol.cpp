class Solution {
public:
    bool isAnagram(string s, string t) {

        int letters[26] = {};

        if (s.length() != t.length()){
            return false;
        }
        for(unsigned int i = 0; i < s.length(); i++){
            letters[int(s[i]) - 97] += 1;
            letters[int(t[i]) - 97] -= 1;
        }

        for(unsigned int i = 0; i < 26; i++){
            if (letters[i] != 0) {
                return false;
            }
        }

        return true; 
    }
};