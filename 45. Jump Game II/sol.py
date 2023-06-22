class Solution(object):
    def jump(self, nums):
        ending_index = 0
        steps = 0
        longest_path = 0

        for i in range(len(nums) - 1):
            longest_path = max(longest_path, nums[i] + i)
            if longest_path >= len(nums) - 1:
                steps += 1
                break
            if ending_index == i:
                ending_index = longest_path
                steps += 1

        return steps      