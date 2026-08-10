class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t : 
            return ""

        left = 0
        s_freq = {}
        t_freq = {}

        for i in t :
            t_freq[i] = t_freq.get(i, 0) + 1
        
        min_length = float("inf")
        min_str = ""

        have, need = 0, len(t_freq)

        for right in range(len(s)) :

            curr = s[right] 
            s_freq[curr] = s_freq.get(curr, 0) + 1

            if curr in t_freq and s_freq[curr] == t_freq[curr] :
                have += 1

            while have == need :
                if right-left+1 < min_length :
                    min_length = right-left+1
                    min_str = s[left: right+1]

                s_freq[s[left]] -= 1
                if s[left] in t_freq and s_freq[s[left]] < t_freq[s[left]] :
                    have -= 1
                
                left += 1

        return min_str

