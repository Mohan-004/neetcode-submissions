class Solution:
    def trap(self, height: List[int]) -> int:
        total_trapped = 0
        n = len(height)
        lefts = [0]*n
        lefts[0] = height[0]
        rights = [0]*n
        rights[-1] = height[-1]
        for i in range(1,n) :
            lefts[i] = max(lefts[i-1], height[i])
        for i in range(n-2,-1,-1) :
            rights[i] = max(rights[i+1], height[i])

        for i in range(n) :
            total_trapped += min(lefts[i], rights[i]) - height[i]

        return total_trapped