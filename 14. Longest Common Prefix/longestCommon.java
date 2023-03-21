import java.util.*;
class Solution {
    public String longestCommonPrefix(String[] strs) {
        Hashtable<String, Integer> my_dict = new  Hashtable<String, Integer>();
        String res = "";
        Arrays.sort(strs);
        String first = strs[0];
        String last = strs[strs.length-1];
        if (first.length() > last.length()){
            for (int i = 0; i < last.length(); i++){
                if (first.charAt(i) == last.charAt(i)) {
                    res += first.charAt(i);
                }
                else{
                    break;
                }
            }
        }else{
            for (int i = 0; i < first.length(); i++){
                if (first.charAt(i) == last.charAt(i)) {
                    res += first.charAt(i);
                }
                else{
                    break;
                }
            }
        }
        return res;
    }
}
