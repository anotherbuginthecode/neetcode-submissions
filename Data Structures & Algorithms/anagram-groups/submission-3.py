class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [[strs[0]]]

        hash_t = {}

        for i, v in enumerate(strs):
            hash_t[i] = {}
            for l in range(len(v)):
                hash_t[i].update({v[l]: 1 + hash_t[i].get(v[l], 0)})

        grouped = []
        tmp = []
        seen = []
        for i in range(0, len(strs)):
            if i not in seen:
                tmp.append(strs[i])
                seen.append(i)
            for j in range(i + 1, len(strs)):
                if hash_t[i] == hash_t[j] and j not in seen:
                    tmp.append(strs[j])
                    seen.append(j)
            if tmp:
                grouped.append(tmp)
                tmp = []

        return grouped