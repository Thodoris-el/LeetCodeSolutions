class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        now = 1
        numberOfDuplicates = 0
        while now < len(nums):
            if nums[start] == nums[now]:
                nums[now] = "_"
                now = now + 1
                numberOfDuplicates = numberOfDuplicates + 1
            else:
                if start + 1 == now:
                    start = start + 1
                    now = now + 1 
                else:
                    nums[start + 1] = int(nums[now])
                    nums[now] = "_"
                    start = start + 1
                    now = now + 1 
        return len(nums) - numberOfDuplicates
