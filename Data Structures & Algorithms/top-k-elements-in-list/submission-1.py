class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}
        out = []

        for i in nums :
            freq_dict[i] = freq_dict.get(i, 0) + 1

        sort_freq_dict = dict(sorted( freq_dict.items(), key = lambda item : item[1], reverse = True))
        for i in sort_freq_dict :
            if k :
                k -= 1
                out.append(i)

        return out


