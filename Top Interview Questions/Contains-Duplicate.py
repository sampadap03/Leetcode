# Easy Collection
# Array
# Languagee : Python3
# Question: https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/578
# Contains Duplicate

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return None
        
        # return True if len(nums) != len(set(nums)) else False
        return len(set(nums)) != len(nums)
        
# hash maps will be usable iff we have to find all duplicates
