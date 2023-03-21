class Solution {
    public boolean isPalindrome(int x) {
        int res = x;
        if (x < 0){
            return false;
        }
        int tmp = x % 10;
        x = x / 10;
        while (x > 0){
            tmp = tmp*10 +  x % 10;
            x = x / 10;
        }
        if ((tmp - res) == 0){
            return true;
        }else{
            return false;
        }
    }
}
