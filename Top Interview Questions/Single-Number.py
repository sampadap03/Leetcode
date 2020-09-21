# Easy Collection
# Array
# Language : python3
# Question : https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/549/
# Single Number
# Statement : Given a non-empty array of integers, every element appears twice except for one. Find that single one.

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_chart = {}
  
        for i in nums:
            try: 
                hash_chart[i] += 1
            except: 
                hash_chart[i] = 1
        
        for i in hash_chart:
            if hash_chart[i] == 1:
                return i
                
# Total runtime: 88ms
# Total memory : 16.2 MB
