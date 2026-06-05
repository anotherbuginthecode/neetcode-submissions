from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ht = Counter(nums)

        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in ht.items():
            buckets[freq].append(num)
        
        out = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                out.append(num)
                if len(out) == k:
                    return out
        