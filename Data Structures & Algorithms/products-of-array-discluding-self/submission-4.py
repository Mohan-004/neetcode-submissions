class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroes = 0
        t_product = 1

        for i in nums :
            if i == 0 :
                zeroes += 1
            else :
                t_product *= i

        if zeroes > 1 :
            return [0]*len(nums)

        f = 1
        if t_product < 0 :
            f = -1


        out = []
        if not zeroes :
            for i in nums :
                    out.append(t_product//i)
        else :
            for i in nums :
                if i == 0 :
                    out.append(t_product)
                else :
                    out.append(0)
        return out


