class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        leftMax = []
        rightMax = []
        length = len(height)
        for i in height:
            leftMax.append(0)
            rightMax.append(0)

        maxl = height[0]
        maxr = height[len(height) - 1]

        for i in range(0, len(height)):
            if maxl < height[i]:
                maxl = height[i]
            if maxr < height[length - 1 - i]:
                maxr = height[length - 1 - i]
            leftMax[i] = maxl
            rightMax[length - 1 - i] = maxr
        
        res = 0
        for i in range(0, length):
            if leftMax[i] < rightMax[i]:
                res = res + leftMax[i] - height[i]
            else:
                res = res + rightMax[i] - height[i]
        
        return res
        
