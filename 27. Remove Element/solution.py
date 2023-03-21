class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        start = 0
        now = 0
        count = 0
        while now < len(nums):
            if nums[now] == val:
                nums[now] = "_"
                now = now + 1
                count = count + 1
            else:
                if start == now:
                    start = start + 1
                    now = now + 1 
                else:
                    nums[start] = int(nums[now])
                    nums[now] = "_"
                    start = start + 1
                    now = now + 1 
        return len(nums) - count
