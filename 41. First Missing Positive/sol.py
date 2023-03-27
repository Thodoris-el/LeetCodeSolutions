class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = {}
        for i in range(1,len(nums)+2):
            res[i] = 0
        for i in nums:
            if i > 0 and i <= len(nums):
                res[i] = 1
        
        for i in res:
            if res[i] == 0:
                return i
