# Easy Collection
# Array
# Languagee : Python3
# Question: https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/578
# Contains Duplicate
# Statement: Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return None
        
        # return True if len(nums) != len(set(nums)) else False
        return len(set(nums)) != len(nums)
        
# hash maps will be usable iff we have to find all duplicates
