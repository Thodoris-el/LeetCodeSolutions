class Solution {
public:
    int lengthOfLastWord(string s) {
        string finalWord = "";

        for (int i = s.length() - 1; i >= 0; i--){
            if(s[i] == ' '){
                if (finalWord == ""){
                    continue;
                }
                return finalWord.length();
            }else{
                finalWord = s[i] + finalWord;
            }
        }
        return finalWord.length();
    }
};