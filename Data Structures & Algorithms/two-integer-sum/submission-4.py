class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ht = {}
        for i,v in enumerate(nums):
            diff = target - v
            if diff in ht: return [ht[diff],i]
            else: 
                ht[v] = i
        return 