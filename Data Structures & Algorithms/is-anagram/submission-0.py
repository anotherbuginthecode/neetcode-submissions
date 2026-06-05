class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        sarr = []
        tarr = []
        for i in s:
            sarr.append(i)
        
        for j in t:
            tarr.append(j)
        
        sarr.sort()
        tarr.sort()

        s = ''.join(sarr)
        t = ''.join(tarr)

        if s == t: return True
        else: return False
        