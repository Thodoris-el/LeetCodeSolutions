class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1,-1]
        if len(nums) == 1:
            if nums[0] == target:
                return [0,0]
            return [-1,-1]
  
        first = 0
        last = len(nums) - 1
        mid = (first + last) // 2

        startingPoint = -2
        endingPoint = -2
        while(first < last):
            if nums[first] == target:
                startingPoint = first
                break
            elif nums[mid] == target:
                if mid == 0 or nums[mid-1] != target:
                    startingPoint = mid
                    break
                else:
                    last = mid
                    mid = (first + last) // 2
            elif nums[last] == target:
                if last-1 >=0 and nums[last-1] != target:
                    startingPoint = last
                    break
                first = mid
                mid = (first + last) // 2
                continue

            elif nums[mid] < target:
                first = mid
                mid = (first + last) // 2
            else:
                last = mid
                mid = (first + last) // 2
            if last-first < 2:
                break

        if startingPoint == -2:
            return [-1,-1]
        
        first = 0
        last = len(nums) - 1
        mid = (first + last) // 2

        while(first < last):
            if nums[last] == target:
                endingPoint = last
                break
            elif nums[mid] == target:
                if mid == len(nums)-1 or nums[mid+1] != target:
                    endingPoint = mid
                    break
                else:
                    first = mid
                    mid = (first + last) // 2
            elif nums[first] == target:
                if first+1 < len(nums) and nums[first] != target:
                    endingPoint = first
                    break
                last = mid
                mid = (first + last) // 2
                continue

            elif nums[mid] < target:
                first = mid
                mid = (first + last) // 2
            else:
                last = mid
                mid = (first + last) // 2
            if last-first < 2:
                break

        if startingPoint == -2:
            return [-1,-1]
        return [startingPoint, endingPoint]
