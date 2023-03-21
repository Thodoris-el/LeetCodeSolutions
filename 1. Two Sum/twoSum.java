import java.util.*;
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] res = {0,0};
        Hashtable<Integer, Integer> my_dict = new Hashtable<Integer, Integer>();
        for (int i = 0; i < nums.length; i++) {
            if (my_dict.get(nums[i]) != null) {
                res[0] = my_dict.get(nums[i]);
                res[1] = i;
                return res;
            }
            else{   
                my_dict.put(target-nums[i], i);
            }
        }
        return res;
    }
}
