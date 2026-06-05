from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1: return [strs]
        ht = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s in ht:
                ht[sorted_s].append(s)
            else:
                ht[sorted_s] = [s]
        
        out = []
        for i in ht:
            out.append(ht[i])
        return out