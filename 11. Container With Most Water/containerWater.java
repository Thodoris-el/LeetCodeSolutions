class Solution {
    public int maxArea(int[] height) {
        int first = 0;
        int last = height.length-1;
        int res = 0;
        int tmp = 0;
        while (first != last){
            tmp = (last - first) * Math.min(height[first], height[last]);
            if (res < tmp){
                res = tmp;
            }
            if (height[first] < height[last]){
                first += 1;
            }
            else{
                last -= 1;
            }
        }
        return res;
    }
}
