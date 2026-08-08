class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        out = [1]*len(nums)

        left_product =  1

        for i in range(len(nums)) :
            out[i] *= left_product
            left_product *= nums[i]

        right_product = 1

        for i in range(len(nums)-1, -1, -1):
            out[i] *= right_product
            right_product *= nums[i]

        return out


