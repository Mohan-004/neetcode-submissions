class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []
        for i in range(len(nums)-1):
            if i > 0 and nums[i-1] == nums[i] :
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right : 
                curr_sum = nums[i]+nums[left]+nums[right]
                if  curr_sum == 0 :
                    out.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left-1] == nums[left] :
                        left += 1
                    while left < right and nums[right+1] == nums[right] :
                        right -= 1
                elif curr_sum < 0 :
                    left += 1 
                else :
                    right -= 1
            
        return out
