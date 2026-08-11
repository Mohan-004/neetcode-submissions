class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        out = [0]*len(temperatures)
        for index, value in enumerate(temperatures) :
            if not stack or stack[-1][0] < value :
                while stack and stack[-1][0] < value:
                    prev_val, prev_ind = stack.pop()
                    out[prev_ind] = (index-prev_ind)
            stack.append((value, index))
        return out