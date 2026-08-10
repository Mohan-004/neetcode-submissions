class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        s1_freq = {}
        for i in s1 :
            s1_freq[i] = s1_freq.get(i,0)+1
        n = len(s1)
        s2_freq = {}
        for right in range(len(s2)):
            s2_freq[s2[right]] = s2_freq.get(s2[right], 0)+1
            if right-left+1 > n :
                s2_freq[s2[left]] -= 1
                if not s2_freq[s2[left]] :
                    del s2_freq[s2[left]]
                left += 1
            if s2_freq == s1_freq :
                return True 
        return False