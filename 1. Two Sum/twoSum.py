class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        result = []
        for i in range(len(nums)):
            if target-nums[i] in dic:
                result.append(dic[target-nums[i]])
                result.append(i)
                return result
            else:
                dic[nums[i]] = i
