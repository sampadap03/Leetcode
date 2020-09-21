# Easy Collection
# Array
# Language : Python3
# Question: https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/727/
# Remove duplicates from sorted array
# Statement: Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length. Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:  
        n = len(nums)
        if not nums:
            return None
        current = 1
        unique = nums[0]
        for i in range(1,n):
            if nums[i] != unique:
                unique = nums[i]
                nums[current] = unique
                current = current + 1
        return current
