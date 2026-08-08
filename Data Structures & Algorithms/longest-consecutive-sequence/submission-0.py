class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        nums_set = set(nums)
        for i in nums_set :
            if i-1 not in nums_set :
                st_char = i 
                while st_char+1 in nums_set :
                    st_char += 1
                longest = max(longest, st_char-i+1)
        return longest