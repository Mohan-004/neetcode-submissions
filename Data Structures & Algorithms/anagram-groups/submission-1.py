class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for s in strs :
            key = {}
            for i in s :
                key[i] = key.get(i, 0) + 1
            key = tuple(sorted(key.items()))
            group.setdefault(key, []).append(s)
        return list(group.values())