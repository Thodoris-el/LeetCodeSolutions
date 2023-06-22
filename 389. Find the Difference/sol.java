class Solution {
    public char findTheDifference(String s, String t) {
        int count = 0;

        for (int i = 0; i < t.length(); i++) {
            count += (int) t.charAt(i);
        }
        for (int i = 0; i < s.length(); i++) {
            count -= (int) s.charAt(i);
        }

        return (char) count;
    }
}