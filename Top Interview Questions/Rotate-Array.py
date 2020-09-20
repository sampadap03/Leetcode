# Easy Collection
# Array
# Language : Python3
# Time: 56 ms (35 test Cases)
# Memory : 15.1 MB
# Question : https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/646
# Rotate Array

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return None
          
        n = len(nums)
        k %= n
        var = nums[-k:]
        nums[k:] = nums[:-k]
        nums[:k] = var
        # self.rotate_set(nums, 0 , n - 1)
        # self.rotate_set(nums,0, k - 1)
        # self.rotate_set(nums, k, n-1)
       
    def rotate_set(self, nums: List[int], l: int, r: int):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l+=1
            r-=1
            
