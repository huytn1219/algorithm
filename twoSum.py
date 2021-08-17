# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Use Hash Table to improve time complexity.

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for idx, val in enumerate(nums):
            if target - val not in seen:
                seen[val] = idx
            else:
                return [seen[target - val], idx]

nums = [2,7,11,15]
target = 9
ob1 = Solution()
print(ob1.twoSum(nums, target))

