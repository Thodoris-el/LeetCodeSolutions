class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
          return -1
        if len(nums) == 1:
          if target == nums[0]:
            return 0
          return -1
        start = 0
        last = len(nums) - 1
        mid = (start + last) // 2
        while(start < last):
            if target == nums[mid]:
                return mid
            if nums[start] == target:
                return start
            if nums[last] == target:
                return last
            if last-start <= 2 :
                return -1
            if nums[start] < nums[mid]:
                if nums[start] < target and target < nums[mid]:
                    last = mid
                    mid = (start + last) // 2
                    continue
            if nums[start] > nums[mid]:
                if (nums[start] < target and target > nums[mid]) or (nums[start] > target and target < nums[mid]):
                    last = mid
                    mid = (start + last) // 2
                    continue
            if nums[mid] < nums[last]:
                if nums[mid] < target and target < nums[last]:
                    start = mid
                    mid = (start + last) // 2
                    continue
            if nums[mid] > nums[last]:
                if (nums[mid] > target and target < nums[last]) or (nums[mid] < target and target > nums[last]):
                    start = mid
                    mid = int((start + last) // 2)
                    continue
            return -1
        return -1
