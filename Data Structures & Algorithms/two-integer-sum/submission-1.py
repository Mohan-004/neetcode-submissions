class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ind_val_dict = {}
        for ind, val in enumerate(nums) :
            diff = target - val 

            if diff in ind_val_dict :
                return [ind_val_dict[diff], ind]

            ind_val_dict[val] = ind