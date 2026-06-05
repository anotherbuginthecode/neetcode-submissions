from collections import defaultdict
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = defaultdict(int)
        most_frequent = defaultdict(int)

        for i in range(len(nums)):
            hm[nums[i]] += 1
        
        ordered_hm = {k: v for k, v in sorted(hm.items(), key=lambda item: item[1], reverse=True)}
        most_frequent = [k for k,v in ordered_hm.items()]
        return most_frequent[:k]


         
